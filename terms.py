import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

st.title('Glossary')

st.markdown('### An explanation of the terms and what they mean')

terms = [
('Solo Staking APR (%)','The APR that a solo staker would get, including execution and consensus layer income.  This is typically around 3%, but will likely decrease as the number of validators increase.'),

('Total Megapool Validators','The number of Rocket Pool validators created in Saturn 1.  Rocket Pool has stood at ~33,000 minipools, but it is not known how many of these will migrate nor how many new validators will be created.'),

('Total RPL Staked in Megapools','The amount of RPL that gets staked in Saturn 1.  Each NO cannot exceed 150% of the value of their megapool staked ETH. Rocket Pool has historically hovered around 10,000,000 staked RPL, but it is not known how much will move to megapools.'),

('Average nETH per Validator','The average amount of nETH required per validator.  This was voted to be 4 for Saturn 1, and can be as low as 1.5 for Saturn 2.  It can change as a result of voting and Nodes adding new minipools.'),

('Voter Share (%)','The percentage of income from validators that goes to voter share.  This was voted to be 9% in Saturn 1.  It can change due to voting.'),

('nETH','Node Operator ETH.  The amount of ETH you use as a bond for staking with Rocket Pool.  '),

("RPL Ratio",f"The value of 1 RPL (in ETH).  It is currently {round(st.session_state['current_rpl_price'], 4)}.  This number is important because you cannot receive income from RPL worth more than 150% of your megapool staked ETH."),

('NO Share (%)','The portion of validator income that goes to NOs for running RP validators.  This was voted to be 5% in Saturn 1.'),

('Number of Validators','The number of validators your node will run.  Assumes you average the same nETH per validator as the protocol (4 for Saturn 1).  '),

('NO Staked RPL','The amount of RPL staked in the megapool by the Node Operator.'),
]

for a, b in terms:
    col1, col2 = st.columns((2, 5))
    col1.markdown(f'**{a}**')
    col2.markdown(b)