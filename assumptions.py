import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

st.title('Assumptions')

"""
In order for the calculator to work, some simplifying assumptions must be made.  They are spelled out here for completeness.
* Ethereum Staking APR remains the same
* No hacks or thefts occur to the Rocket Pool protocol 
* The protocol functions as spelled out in the RPIPs as of January 26, 2025

The calculators follow my best understanding of what we should expect in Saturn 1 and 2.  I make no guaruntees as to the accuracy of these figures.

"""