 # Importing required packages
import streamlit as st
import pandas as pd
import altair as alt

import page_one
import page_two


st.title('Multi-Page Marketing App')

PAGES = {
    "Page one": page_one,
    "Page two": page_two
    }



st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()
