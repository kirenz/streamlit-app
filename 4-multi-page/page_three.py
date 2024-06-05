import streamlit as st
from my_data import df
from streamlit_chart import c

def app():
    st.title('Kennzahlen')

    st.dataframe(df)

    st.altair_chart(c, use_container_width=True)

if __name__ == "__main__":
    app()
