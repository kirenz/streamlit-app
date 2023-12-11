 # Importing required packages
import streamlit as st
import openai
import uuid
import time
import pandas as pd
import io
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

import user_persona
import company_info
import openai_model


st.title('Multi-Page Marketing App')

PAGES = {
    "User Persona Creation": user_persona,
    "Company Information": company_info,
    "OpenAI Model": openai_model
}



st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()
