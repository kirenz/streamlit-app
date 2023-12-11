 # Importing required packages
import streamlit as st
import pandas as pd
import altair as alt

import page_one
import page_two
from my_data import df
from streamlit_chart import c


st.title('Multi-Page App')

PAGES = {
    "Page one": page_one,
    "Page two": page_two
    }



st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]

st.dataframe(df)

st.altair_chart(c, use_container_width=True)


page.app()
