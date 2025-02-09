import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

st.image('./data/icon.png') 

st.session_state['disclaimer'] = True




"""

# Rocket Pool Fee Switch Calculator

The sidebar on the left allows access to calculators and resources for Rocket Pool Node Operators.

1. Saturn 1 Voter Share""" 

# st.page_link("staking.py", label = "Saturn 1 Voter Share") 

""" About how much ETH will you get per month from voter share during Saturn 1?

2. RPL Ratio 

What would you value RPL at?  Calculator your ratio for a given required ROI

3. Voter Share vs Burn - Shouldn't do
"""

# Add some spacing
''
''