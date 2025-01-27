import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

st.title('ETH Flow per Year')
"""Placeholder for a potential second calculator"""
col1, col2, col3 = st.columns(3)
solo_staking_apr =col1.number_input('Solo Staking APR (%)', value = 3.)
validators = col2.number_input('Total number of validators in megapools', value = 30000)
nETH_per =col1.number_input('Average nETH per Validator', value = 4.)
total_staked_RPL = col3.number_input('RPL Staked in Megapools', value = 11000000)
voter_share = col2.number_input('Voter Share (%)', value = 6.)
surplus_share = col3.number_input('Surplus Share (%)', value = 0.05)
eth_price = col1.number_input('ETH Price ($)', value = 3300)

st.header('ETH Flow per Year per RPL', divider='gray')