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
st.markdown("With the tokenomics overhaul in Rocket Pool, the way the protocol generates income will be changing!  The changes will take place in two phases: Saturn 1 and Saturn 2.  Saturn 1 will allow for the creation of megapools (using 4 ETH bonds), with income going to rETH holders, Node Operators, and RPL stakers.  Saturn 2 will expand on this, allowing for even lower ETH bonds and potentially further income streams (voting has not yet occurred).")
st.markdown("This app is an attempt to explain the mechanics in simple terms and also allow users to estimate things like income or APR in the new system.")
st.markdown("## Navigation")
"""
The sidebar on the left allows access to calculators and resources for Rocket Pool Node Operators.

##### Saturn 1 Voter Share""" 

# st.page_link("pages/S1_staking.py", label = "## Saturn 1 Voter Share") 

""" About how much ETH will you get per month from voter share during Saturn 1?  Also includes normal staking income and RPL issuance rewards.

##### Saturn 2 Staking

**Waiting on Saturn 2 Vote!**  Placeholder when Saturn 2 plans are finalized.

##### Assumptions

The assumptions calculators need to make in order to estimate future states.

##### Glossary

Confused by any terms?  Check here for a more thorough explanation or more information!
"""
''
''
''
''
''
''
''


S1_staking.display_page()
assumptions.display_page()
terms.display_page()
feedback.display_page()
