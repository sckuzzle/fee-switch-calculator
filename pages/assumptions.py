import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

def display_page():
    st.title('Assumptions')

    st.markdown("In order for the calculator to work, some simplifying assumptions must be made.  They are spelled out here for completeness.")
    st.markdown("* Ethereum Staking APR remains the same")
    st.markdown("* No hacks or thefts occur to the Rocket Pool protocol ")
    st.markdown("* The protocol functions as spelled out in the RPIPs as of January 26, 2025")

    st.markdown("The calculators follow my best understanding of what we should expect in Saturn 1 and 2.  I make no guaruntees as to the accuracy of these figures.")
    

display_page()