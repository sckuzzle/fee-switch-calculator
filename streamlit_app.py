import streamlit as st
import pandas as pd
import math
import plotly.graph_objects as go
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='RPL Fee Switch Calculator',
    page_icon='https://rocketpool.net/files/rp-logo-200x200.png')


# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
pg = st.navigation({'Calculators': [st.Page("home.py", title = 'Home'), 
                                    st.Page("staking.py", title = 'Staking'), 
                                    st.Page('ETH_flow.py', title = 'ETH Flow'),
                                    ],
                    'Resources':[st.Page('assumptions.py', title = 'Assumptions'),
                                 st.Page('terms.py', title = 'Terms'),
                                 ],
                    }, expanded = True)


# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )




pg.run()

''

# st.line_chart(
#     filtered_gdp_df,
#     x='Year',
#     y='GDP',
#     color='Country Code',
# )

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=GDP_plot[country]['Year'], y = GDP_plot[country]['GDP'],
#                     mode='lines',
#                     name=country))
# st.plotly_chart(fig)

''
''


