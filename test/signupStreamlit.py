import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from config.database import Database
from page.signup_page import render_signup_page

st.set_page_config(page_title="Streamlit Signup Test", layout="centered")

Database.initialize()

render_signup_page()