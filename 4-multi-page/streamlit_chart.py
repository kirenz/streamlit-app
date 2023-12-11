 # Importing required packages
import streamlit as st
import pandas as pd
import altair as alt

from my_data import df

c = alt.Chart(df).mark_bar().encode(
    x='country',
    y='life_satisfaction',
    tooltip = ['country', "life_satisfaction"]
)