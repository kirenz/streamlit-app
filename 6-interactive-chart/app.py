# -------------------#
# SETUP
import streamlit as st
import pandas as pd
import altair as alt

# -------------------#
# IMPORT DATA

df = pd.read_csv(
    "https://raw.githubusercontent.com/kirenz/datasets/master/oecd-new.csv")

### -------------------###
# START OF OUR APP

# -------------------#
# HEADER
# Title of our app
st.title("Hello World")
# Add header
st.header("My Text")
# -------------------#
# SIDEBAR
# Header
st.sidebar.header("This is my sidebar")
# MULTISELECT
COUNTRY = df['country'].to_list()
#selected_country = COUNTRY
selected_country = st.sidebar.multiselect(
    'Select', COUNTRY)
# Filter the DataFrame based on the selected countries
filtered_df = df[df['country'].isin(selected_country)]

# -------------------#
# BODY

# Check if the user has made a selection
if selected_country:
    # If the user has selected countries, filter the DataFrame
    filtered_df = df[df['country'].isin(selected_country)]
else:
    # If no selection is made, use the complete DataFrame
    filtered_df = df
    
st.write("Take a look at my data")
# Show filtered DataFrame
st.dataframe(filtered_df)

st.write("Take a look at my chart")
# Make a chart with altair

c = alt.Chart(filtered_df).mark_circle().encode(
    x='life_satisfaction',
    y='gdp_per_capita',
    color='country'
)

# Show plot
st.altair_chart(c, use_container_width=True)

### -------------------###

st.write("Take a look at my interactive chart")
# Make a chart with altair
highlight = alt.selection_point(on='mouseover', fields=['symbol'], nearest=True)

base = alt.Chart(source).encode(
    x='life_satisfaction',
    y='gdp_per_capita',
    color='country'
)

points = base.mark_circle().encode(
    opacity=alt.value(0)
).add_params(
    highlight
).properties(
    width=600
)

lines = base.mark_line().encode(
    size=alt.condition(~highlight, alt.value(1), alt.value(3))
)

points + lines



# END OF APP
