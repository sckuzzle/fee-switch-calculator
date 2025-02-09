import os
import math

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
from web3 import Web3, HTTPProvider

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Rocket Pool Fee Switch Calculator',
    page_icon='https://rocketpool.net/files/rp-logo-200x200.png')


# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.



# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )


def set_state():
    ARCHIVE_NODE_IP = os.environ['archive_node_ip']
    
    CLIENT = Web3(Web3.HTTPProvider(f'{ARCHIVE_NODE_IP}'))

    RocketNetworkPrices = CLIENT.eth.contract(
        address=Web3.to_checksum_address("0x25E54Bf48369b8FB25bB79d3a3Ff7F3BA448E382"),
        abi=
        '[{"inputs":[{"internalType":"contract RocketStorageInterface","name":"_rocketStorageAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rplPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"PricesSubmitted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rplPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"PricesUpdated","type":"event"},{"inputs":[{"internalType":"uint256","name":"_block","type":"uint256"},{"internalType":"uint256","name":"_rplPrice","type":"uint256"}],"name":"executeUpdatePrices","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getLatestReportableBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPricesBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRPLPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_block","type":"uint256"},{"internalType":"uint256","name":"_rplPrice","type":"uint256"}],"name":"submitPrices","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"}]'
        )
    rpl_price_in_eth = RocketNetworkPrices.functions.getRPLPrice().call() / 1e18
    st.session_state['current_rpl_price'] = rpl_price_in_eth
    st.session_state['disclaimer'] = True



if 'disclaimer' not in st.session_state:
    st.session_state['disclaimer'] = False



if st.session_state['disclaimer']:
    pg = st.navigation({'Calculators': [st.Page("home.py", title = 'Home'), 
                                    st.Page("staking.py", title = 'Saturn 1 Staking'), 
                                    st.Page('ETH_flow.py', title = 'Placeholder Calc'),
                                    ],
                    'Resources':[st.Page('assumptions.py', title = 'Assumptions'),
                                    st.Page('terms.py', title = 'Terms'),
                                    ],
                    }, expanded = True)
    pg.run()
else:
    st.markdown('# Rocket Pool Fee Switch Calculator')
    st.markdown('## Disclaimer')
    st.markdown('This is a speculative calculator!  It allows you to input what you think will happen with Rocket Pool in Saturn 1 and then calculate the amount of income Node Operators staking RPL would expect to get as a result.  Default values are provided that should be in the right ballpark, but you can (and should!) adjust them!')
    st.button("I understand.", on_click = set_state)
    if st.session_state['disclaimer']:
        st.rerun()


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


