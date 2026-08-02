import streamlit as st
import random
import time  # 🎯 هذا هو السطر اللي كان ناقص وحل المشكلة!
from repo.userRepo import UserRepository

def apply_login_css_and_floating_icons():
    # 1. مصفوفة تحتوي على كلاسات FontAwesome الخاصة بالتحليل والداتا
    icons_classes = [
        "fa-solid fa-chart-line", 
        "fa-solid fa-chart-pie", 
        "fa-solid fa-chart-bar", 
        "fa-solid fa-database", 
        "fa-solid fa-server", 
        "fa-solid fa-code", 
        "fa-solid fa-brain",
        "fa-solid fa-microchip",
        "fa-solid fa-magnifying-glass-chart",
        "fa-solid fa-laptop-code"
    ]
    
    # 2. توليد عناصر الـ HTML للأيقونات الطائرة بحركة عشوائية في كل الاتجاهات
    floating_divs = []
    for i in range(25):
        icon_class = random.choice(icons_classes)
        left = random.randint(5, 95)
        top = random.randint(5, 95)
        delay = random.randint(0, 10)
        duration = random.randint(20, 35)
        size = random.randint(16, 26)
        opacity = round(random.uniform(0.12, 0.28), 2)
        
        anim_name = f"randomMove{i % 4}" 
        
        style = f"left:{left}%; top:{top}%; animation:{anim_name} {duration}s linear -{delay}s infinite; font-size:{size}px; opacity:{opacity};"
        floating_divs.append(f'<div class="floating-icon" style="{style}"><i class="{icon_class}"></i></div>')
    
    icons_html = "".join(floating_divs)

    st.markdown(f'<div class="floating-background">{icons_html}</div>', unsafe_allow_html=True)

    # 3. حقن الـ CSS الكامل
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    .floating-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        overflow: hidden;
        pointer-events: none;
    }

    .floating-icon {
        position: absolute;
        color: #6dabe4;
    }

    @keyframes randomMove0 {
        0%   { transform: translate(0, 0) rotate(0deg); }
        25%  { transform: translate(40px, -60px) rotate(90deg); }
        50%  { transform: translate(-20px, -120px) rotate(180deg); }
        75%  { transform: translate(-50px, -40px) rotate(270deg); }
        100% { transform: translate(0, 0) rotate(360deg); }
    }

    @keyframes randomMove1 {
        0%   { transform: translate(0, 0) rotate(0deg); }
        33%  { transform: translate(-60px, 40px) rotate(-120deg); }
        66%  { transform: translate(5px, -80px) rotate(-240deg); }
        100% { transform: translate(0, 0) rotate(-360deg); }
    }

    @keyframes randomMove2 {
        0%   { transform: translate(0, 0) rotate(0deg); }
        25%  { transform: translate(-30px, -50px) rotate(90deg); }
        50%  { transform: translate(50px, 20px) rotate(180deg); }
        75%  { transform: translate(-20px, 60px) rotate(270deg); }
        100% { transform: translate(0, 0) rotate(360deg); }
    }

    @keyframes randomMove3 {
        0%   { transform: translate(0, 0) rotate(0deg); }
        50%  { transform: translate(70px, -70px) rotate(180deg); }
        100% { transform: translate(0, 0) rotate(360deg); }
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Poppins', sans-serif !important;
        background-color: #f8f8f8 !important;
    }

    footer { visibility: hidden !important; }

    div[data-testid="stHorizontalBlock"] {
        background: #ffffff !important;
        border-radius: 20px !important;
        box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.05) !important;
        max-width: 900px !important;
        margin: 40px auto !important;
        padding: 40px 50px !important;
        position: relative !important;
        z-index: 10 !important;
        align-items: center !important;
    }

    div[data-testid="stForm"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0px !important;
    }

    div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid #999999 !important;
        border-radius: 0px !important;
        box-shadow: none !important;
        padding: 4px 0px !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-bottom: 2px solid #222222 !important;
    }

    div[data-baseweb="input"] > div { background-color: transparent !important; border: none !important; }
    input { color: #222222 !important; font-size: 14px !important; }
    div[data-testid="stWidgetLabel"] p { color: #222222 !important; font-weight: 500 !important; font-size: 13px !important; }

    div[data-testid="stFormSubmitButton"] > button {
        background-color: #6dabe4 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 12px 40px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        margin-top: 20px !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover { background-color: #4292dc !important; }

    div[data-testid="stColumn"] button[kind="tertiary"],
    div[data-testid="stColumn"] button[type="secondary"] {
        background: transparent !important;
        border: none !important;
        color: #222222 !important;
        text-decoration: underline !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        box-shadow: none !important;
        margin: 20px auto 0px auto !important;
        display: block !important;
        padding: 0px !important;
    }
    div[data-testid="stColumn"] button:hover { color: #4292dc !important; }
    </style>
    """, unsafe_allow_html=True)

def render_login_page():
    apply_login_css_and_floating_icons()

    col_left, col_right = st.columns([0.9, 1.1], gap="large")

    with col_left:
        st.image(
            "https://colorlib.com/etc/regform/colorlib-regform-7/images/signin-image.jpg",
            use_container_width=True
        )
        if st.button("Create an account", key="go_to_signup", type="tertiary"):
            st.session_state['page'] = 'signup'
            st.rerun()

    with col_right:
        with st.form("login_form", clear_on_submit=False):
            st.markdown("<h2 style='font-size: 30px; font-weight: 700; color: #222222; margin-bottom: 25px;'>Sign in</h2>", unsafe_allow_html=True)
            email = st.text_input("Your Email", placeholder="Your Email")
            password = st.text_input("Password", type="password", placeholder="Password")
            remember_me = st.checkbox("Remember me")
            submit_button = st.form_submit_button("Log in")

    if submit_button:
        if not email or not password:
            st.error("Please fill in both email and password.")
            return

        user_repo = UserRepository()
        result = user_repo.login_user(email, password)

        if result.get("status") == "success":
            st.success(f"Welcome back, {result.get('full_name')}!")
            st.session_state['user_name'] = result.get('full_name')
            st.session_state['page'] = 'dashboard'
            time.sleep(1)
            st.rerun()
        else:
            st.error(result.get("message"))