import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

st.title('Staking')
"""ETH Flow from RPL for NOs Saturn 1"""

col1, col2, col3 = st.columns(3)
solo_staking_apr =col1.number_input('Solo Staking APR (%)', value = 3.)
validators = col2.number_input('Total validators in megapools', value = 30000)
total_staked_RPL = col3.number_input('RPL Staked in Megapools', value = 11000000)

col1, col2, col3 = st.columns(3)
nETH_per =col1.number_input('Average nETH per Validator', value = 4.)
voter_share = col2.number_input('Voter Share (%)', value = 9.)
surplus_share = col3.number_input('Surplus Share (%)', value = 0.0)

col1, col2, col3 = st.columns(3)
eth_price = col1.number_input('ETH Price ($)', value = 3300)
NO_pools = col2.number_input('Number of 4 ETH minipools', value = 1)


st.header('ETH Flow per Year per RPL', divider='gray')

net_voter_flow = (32-nETH_per)*validators*solo_staking_apr*voter_share/100
flow_per_RPL = net_voter_flow / total_staked_RPL

@st.cache_data
def get_staked_rpl_curve():
    """If I add a comment here what happens?  No magic please"""
    rewards_rate = []
    for n in range(200):
        if n > 150:
            n = 150
        rewards_rate.append(n)
    rewards_rate = np.array(rewards_rate, dtype = np.float64)
    return rewards_rate

rewards_curve = get_staked_rpl_curve()
rewards_curve = flow_per_RPL * rewards_curve


fig = go.Figure()
fig.add_trace(go.Scatter(x=4*NO_pools*np.arange(200)/100, y = rewards_curve,
                    mode='lines',
                    name="RPL rewards"))
fig.update_layout(xaxis_title = 'ETH value of Megapool staked RPL',
                  yaxis_title = 'ETH per Year')
st.plotly_chart(fig)
        
