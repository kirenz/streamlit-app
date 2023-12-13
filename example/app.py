# SETUP
import streamlit as st
import pandas as pd
import altair as alt

# IMPORT DATA
LINK = 'https://raw.githubusercontent.com/kirenz/datasets/master/oecd-new.csv'
df = pd.read_csv(LINK)

###--------------------------###
###--------------------------###
# START OF OUR APP 

# TITLE
st.title('Hello World!!👋')

# MARKDOWN EXAMPLES
st.markdown('![](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGw5bTR5Y2k5MnYxcXkxaXF2Ymxwa2c5ODAxbDVpZmZkb2M3MGk1cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Grwq4Z2Q41bVbAQJc5/giphy.gif)')

st.markdown('Blumen :tulip::skull:')

st.markdown('''

## H2 Überschrift

Beispiel mit mehreren Zeilen. Dies ist *kursiver* Text, bzw. **fett** ...

1. dies
1. ist 
1. eine Aufzählung

:red[Dieser Text wird rot angezeigt]

:rainbow[Hier sehen wir Regenbogenfarben]

'''
)
###--------------------------###
# SHOW DATAFRAME
st.write('Take a look at my data:')
st.dataframe(df)
# or you can use this for a static version
st.table(df)

###--------------------------###
# SHOW ALTAIR CHART
chart = alt.Chart(df).mark_circle().encode(
    x='life_satisfaction',
    y='gdp_per_capita',
    color='country'
)

# we us use_container_width=True to use the full screen
st.altair_chart(chart, use_container_width=True)

###--------------------------###
# SIDEBAR

st.sidebar.header('This is my Sidebar')

satisfaction = st.sidebar.slider('What is your satisfaction...?', 0, 10, 1)

st.sidebar.write('Your satisfaction is around', satisfaction, 'points')