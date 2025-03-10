import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

import pages.S1_staking as S1_staking
import pages.terms as terms
import pages.assumptions as assumptions
import pages.feedback as feedback

st.image('./data/icon.png', width = 80) 

# st.session_state['disclaimer'] = True
st.title("Rocket Pool Fee Switch Calculators")
st.markdown("With the tokenomics overhaul in Rocket Pool, income generation will be changing!  The changes will take place in two phases: Saturn 1 and Saturn 2.  Saturn 1 will allow for the creation of megapools (using 4 ETH bonds), with income going to rETH holders, Node Operators, and RPL stakers.  Saturn 2 will expand on this, allowing for even lower ETH bonds and potentially further income streams (voting has not yet occurred).")
st.markdown("This app is an attempt to explain the mechanics in simple terms and also allow users to estimate things like income or APR in the new system.")
st.markdown("## Navigation")
"""
The sidebar on the left allows access to calculators and resources for Rocket Pool Node Operators.
"""

navigation = [
            ('**Saturn 1 Voter Share**', 'pages/S1_staking.py', 'About how much ETH will you get per month from voter share during Saturn 1?  Also includes normal staking income and RPL issuance rewards.'),
            ('**Saturn 2 Staking**', 'pages/S2_staking.py', '**Waiting on Saturn 2 Vote!**  Placeholder when Saturn 2 plans are finalized.'),
            ('**Assumptions**', 'pages/assumptions.py', 'The assumptions calculators need to make in order to estimate future states.'),
            ('**Glossary**', 'pages/terms.py', 'Confused by any terms?  Check [here](#anchor) for a more thorough explanation or more information!'),
            ('**Feedback**', 'pages/feedback.py', 'Links to a place where you can ask questions or give feedback.'),
            ]

for a, link, b in navigation:
    col1, col2 = st.columns((2, 5))
    col1.page_link(link, label = a)
    col2.markdown(b)


S1_staking.display_page()
assumptions.display_page()
terms.display_page()
feedback.display_page()
