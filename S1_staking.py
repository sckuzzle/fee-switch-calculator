import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

st.title('Rocket Pool Saturn 1 Staking Calculator')
"""This calculator allows you to calculate the income and APR you would get from running a Rocket Pool Node in Saturn 1.  Since income will depend on factors that will not be live until Saturn 1, we must speculate on what these will be to create estimates."""


st.markdown("## Rocket Pool Estimates")

st.markdown("In Saturn 1, a portion of megapool validator income will go to Node Operators (NOs) who stake RPL.  The APR will heavily depend on the total amount of megapool validators and the amount of megapool staked RPL, which do not exist yet. Input your estimations below!")

col1, col2= st.columns(2)
total_validators = col2.number_input('Total Megapool Validators', min_value = 1, value = 20000, help = "The number of Rocket Pool validators created in Saturn 1.  More validators results in more ETH income to RPL stakers. ")
total_staked_RPL = col1.number_input('Total RPL Staked in Megapools', min_value = 1, value = 8000000, help = "The amount of RPL that gets staked in Saturn 1.  Each NO cannot exceed 150% of the value of their megapool staked ETH.  More staked RPL will dilute the rewards to RPL stakers.")

with st.expander('Advanced Rocket Pool Settings'):
    st.markdown('These settings are either not expected to change or are not as important.  However, they are included here if you want to play with them anyway.')
    col1, col2, col3 = st.columns(3)
    NO_share = col1.number_input('NO Share (%)', value = 5., min_value = 0., step = 1., format="%.1f", help = "The portion of validator income that goes to NOs for running RP validators.  This was voted to be 5% in Saturn 1")
    voter_share = col2.number_input('Voter Share (%)', value = 9., step = 1., min_value = 0., format="%.1f", help = "The percentage of income from staked protocol ETH that goes to voter share.  This was voted to be 9% in Saturn 1")
    rpl_ratio = col3.number_input('RPL Ratio', value = st.session_state['current_rpl_price'], min_value = 0.000001, format="%.4f", step = 0.0001, help = "The value of 1 RPL (in ETH).  The RPL ratio affects how much RPL you can stake on your node (you cannot exceed 150% of the value of your staked ETH).")

    col1, col2 = st.columns([1, 2])
    solo_staking_apr =col1.number_input('Solo Staking APR (%)', value = 3., step = 0.1, help='The APR that a solo staker gets')
    nETH_per =col2.number_input('Average ETH Bond per Validator', value = 4., min_value = 1., step = 0.1, help = "The average amount of Node-Operator staked ETH (nETH) required per validator.  This is the bond that Operators put up to create minipools, and is expected to be 4 for Saturn 1 and smaller for Saturn 2. The amount of nETH per validator affects how much protocol ETH is staked and how much income goes to RPL stakers.  Note that we still expect validators to be 32 ETH total each.")
    
# Per interval
net_voter_flow = (32-nETH_per)*total_validators*(solo_staking_apr/100)*(voter_share/100)*28/365
flow_per_RPL = net_voter_flow / total_staked_RPL

st.markdown(f"If there are {total_validators} megapool validators and {total_staked_RPL} RPL staked:")
st.markdown(f"The total amount of ETH flowing to voters is **:blue[{round(net_voter_flow, 1)}]** ETH every interval (28 days). This means that each effectively staked RPL receives **:blue[{str(format(flow_per_RPL, 'f'))}]** ETH per interval.")


st.markdown("## Node Operator (NO) Estimates")
col1, col2 = st.columns(2)
NO_pools = col1.number_input('Number of Validators', value = 1, min_value = 1, help = f"The number of validators your node will run.  Assumes you average the same nETH per validator as the protocol (currently set to {round(nETH_per, 2)})")
staked_RPL = col2.number_input('NO Staked RPL', value = 0., help = "The amount of RPL staked in the megapool by the Node Operator")

#NO Calculations
validator_income = NO_pools*(nETH_per+(32-nETH_per)*NO_share/100)*solo_staking_apr/100*28/365
percent_of_max = staked_RPL*rpl_ratio / (1.5*4*NO_pools)*100
effective_RPL = min(1.5*4*NO_pools/rpl_ratio, staked_RPL)
RPL_income = flow_per_RPL*effective_RPL
total_income = validator_income + RPL_income
income_APR = total_income / (NO_pools*nETH_per + rpl_ratio*staked_RPL)*365/28*100
theoretical_RPL_APR = flow_per_RPL / rpl_ratio * 365/28*100

# Ratio when RPL rewards start to drop off
issuance_ratio = 0.15 * (32-nETH_per)/nETH_per

@st.cache_data
def get_staked_rpl_curve():
    """If I add a comment here what happens?  No magic please"""
    rewards_rate = []
    for n in range(200):
        if n > 150:
            n = 150
        rewards_rate.append(n/150)
    rewards_rate = np.array(rewards_rate, dtype = np.float64)
    return rewards_rate

rewards_curve = get_staked_rpl_curve()
rewards_curve = flow_per_RPL * rewards_curve * 1.5*4*NO_pools/rpl_ratio
x = 4*NO_pools*np.arange(200)/100/rpl_ratio

if staked_RPL > 4*NO_pools*1.5/rpl_ratio:
    x= np.append(x, staked_RPL)
    rewards_curve = np.append(rewards_curve, rewards_curve[-1])

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y = rewards_curve,
                    mode='lines',
                    name="RPL rewards"))
fig.add_vline(x= percent_of_max/100*4*NO_pools*1.5/rpl_ratio, line_color = 'green', line_dash = 'dash', annotation_text = 'Your Staked RPL')
fig.add_vline(x= issuance_ratio * 4*NO_pools/rpl_ratio, line_color = 'blue', line_dash = 'dash', annotation_text = 'RPL Reward Dropoff')
fig.update_layout(xaxis_title = 'Staked RPL',
                  yaxis_title = 'ETH income per 28 days',
                  title = {'text':'Staked RPL Income Flow',
                        'xanchor':'center', 
                        'x':0.5})

full_reward_string = f"You could stake up to **:blue[{round(4*NO_pools*1.5/rpl_ratio-staked_RPL)}]** more RPL that would be eligible for voter share and **:blue[{round(4*NO_pools*issuance_ratio/rpl_ratio-staked_RPL)}]** more RPL before RPL issuance rewards drop off!"
if staked_RPL*rpl_ratio> 1.5*4*NO_pools:
    st.markdown(f'**:red[WARNING]:** Your effectively staked RPL for voter share is being limited to 150% of your nETH.  Either increase your staking validators or stake less RPL to receive full voter share income from your RPL.')
if staked_RPL == 0:
    st.markdown(f"Your proposed node staking would receive about **:blue[{round(total_income, 3)}]** ETH per 28 days (**:blue[{round(income_APR, 2)}]**% APR).  You are not staking RPL, but it would receive about **:blue[{round(theoretical_RPL_APR, 2)}]**% APR")
    st.plotly_chart(fig)
    st.markdown(full_reward_string)
else:
    # RPL Issuance
    borrowed_eth = (32-nETH_per)*NO_pools
    if staked_RPL*rpl_ratio/borrowed_eth > 0.15:
        weight = (13.6137+2*math.log(100*staked_RPL*rpl_ratio/borrowed_eth-13))*borrowed_eth/(100*rpl_ratio)
    else:
        weight = staked_RPL
    rpl_rewards = weight * 0.0733*28/365

    validator_apr = validator_income*365/28/(NO_pools*nETH_per)*100
    rpl_apr = (RPL_income)*365/28/(rpl_ratio*staked_RPL)*100
    st.markdown(f"Your proposed node staking would receive about **:blue[{round(total_income, 3)}]** ETH per 28 days (**:blue[{round(income_APR, 2)}]**% APR).  Of this, **:blue[{round(RPL_income, 4)}]** ETH is coming from the staked RPL (**:blue[{round(rpl_apr, 2)}]**% APR),  and **:blue[{round(validator_income, 3)}]** ETH from your validators (**:blue[{round(validator_apr, 2)}]**% APR).")
    st.markdown(f'Additionally, you can expect to receive about **:blue[{round(rpl_rewards, 2)}]** RPL per 28 days if the RPL issuance rewards rate continues (historically, ~7.33% APR on effectively staked RPL).')
    st.plotly_chart(fig)

    if staked_RPL*rpl_ratio/borrowed_eth > 0.15:
        if staked_RPL < 4*NO_pools*1.5/rpl_ratio:
            # RPL issuance dropoff, less than max voter share
            st.markdown(f"You could stake up to **:blue[{round(4*NO_pools*1.5/rpl_ratio-staked_RPL)}]** more RPL that would be eligible for voter share!")
        else:
            # Above max effectively staked
            st.markdown(f"You have more staked RPL than can be effectively staked.")
    else:
        # Room for both more RPL issuance and voter share
        st.markdown(full_reward_string)
        
        
st.html("<style> .main {overflow: hidden} </style>")
