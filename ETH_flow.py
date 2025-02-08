import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

st.title('ETH Flow per Year')
"""Placeholder for a potential second calculator"""
col1, col2, col3 = st.columns(3)
solo_staking_apr =col1.number_input('Solo Staking APR (%)', value = 3., step = 0.1, help='The APR that a solo staker gets')
total_validators = col2.number_input('Total validators in megapools', min_value = 1, value = 30000, help = "The number of Rocket Pool validators created in Saturn 1")
total_staked_RPL = col3.number_input('RPL Staked in Megapools', min_value = 1, value = 11000000, help = "The amount of RPL that gets staked in Saturn 1.  Each NO cannot exceed 150% of the value of their megapool staked ETH")

col1, col2, col3 = st.columns(3)
nETH_per =col1.number_input('Average nETH per Validator', value = 4., min_value = 1., step = 0.1, help = "The average amount of nETH required per validator.  This is expected to be 4 for Saturn 1, and will be smaller for Saturn 2.")
voter_share = col2.number_input('Voter Share (%)', value = 9., step = 1., min_value = 0., format="%.1f", help = "The percentage of income from validators that goes to voter share.  This was voted to be 9% in Saturn 1")
surplus_share = col3.number_input('Surplus Share (%)', value = 0.0, format="%.4f", min_value = 0., step = 1., help = "The percentage of income that goes to the surplus revenue stream.  This will be 0 for Saturn 1")

col1, col2, col3 = st.columns(3)
eth_price = col1.number_input('ETH Price ($)', value = 3300)
NO_pools = col2.number_input('Number of validators', value = 1, min_value = 1, help = f"The number of validators your node will run.  Assumes you average the same nETH per validator as the protocol (currently set to {round(nETH_per, 2)})")
rpl_ratio = col3.number_input('RPL Ratio', value = 0.003, min_value = 0.000001, format="%.4f", step = 0.0001, help = "The value of 1 RPL (in ETH)")

col1, col2, col3 = st.columns(3)
NO_share = col1.number_input('NO Share (%)', value = 5., min_value = 0., step = 1., format="%.1f", help = "The portion of validator income that goes to NOs.  This was voted to be 5% in Saturn 1")
staked_RPL = col2.number_input('NO Staked RPL', value = 0., help = "The amount of RPL staked on the megapool by the Node Operator")


st.header('ETH Flow per Year per RPL', divider='gray')