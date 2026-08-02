import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from config.database import Database
from page.signup_page import render_signup_page
from page.login_page import render_login_page
from page.dashboard_page import render_dashboard_page # استدعاء الصفحة الجديدة

st.set_page_config(page_title="Data Analytics System", layout="wide") # خليناها wide عشان رسومات التحليل تاخذ راحتها

Database.initialize()

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# نظام التنقل الثلاثي
if st.session_state['page'] == 'login':
    render_login_page()
elif st.session_state['page'] == 'signup':
    render_signup_page()
elif st.session_state['page'] == 'dashboard':
    render_dashboard_page()