import streamlit as st
import datetime
import pycountry
from model.user import User
from repo.userRepo import UserRepository

# Get list of countries
COUNTRIES = [country.name for country in pycountry.countries]
GENDERS = ["Male", "Female", "Other"]

def apply_colorlib_regform7_css():
    st.markdown("""
    <!-- Import Poppins Font & FontAwesome Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
    /* Reset & Fonts */
    html, body, [class*="css"], .stApp {
        font-family: 'Poppins', sans-serif !important;
        background-color: #f8f8f8 !important;
    }

    /* Hide Streamlit Header & Footer */
    

    /* Main Container Card (WIDER LAYOUT) */
    div[data-testid="stForm"] {
        background: #ffffff !important;
        border-radius: 20px !important;
        box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.05) !important;
        border: none !important;
        max-width: 1100px !important;  
        margin: 30px auto !important;
        padding: 50px 60px !important;
    }

    /* Input Base Style */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid #999999 !important;
        border-radius: 0px !important;
        box-shadow: none !important;
        padding: 2px 0px !important;
    }

    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-bottom: 2px solid #222222 !important;
    }

    div[data-baseweb="input"] > div, 
    div[data-baseweb="select"] > div {
        background-color: transparent !important;
        border: none !important;
    }

    /* Inputs Text & Color */
    input {
        color: #222222 !important;
        font-size: 13px !important;
        font-family: 'Poppins', sans-serif !important;
    }

    input::placeholder {
        color: #999999 !important;
    }

    div[data-testid="stWidgetLabel"] p {
        color: #222222 !important;
        font-weight: 500 !important;
        font-size: 13px !important;
        margin-bottom: 2px !important;
    }

    /* Button Styling */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #6dabe4 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 12px 40px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        margin-top: 15px !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #4292dc !important;
        box-shadow: 0px 8px 15px rgba(109, 171, 228, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def render_signup_page():
    apply_colorlib_regform7_css()

    repo = UserRepository()

    with st.form("signup_form", clear_on_submit=False):
        # Increased column ratio for inputs to give more breathing room
        col_left, col_right = st.columns([1.3, 0.9], gap="large")

        with col_left:
            st.markdown("<h2 style='font-size: 32px; font-weight: 700; color: #222222; margin-bottom: 20px;'>Sign up</h2>", unsafe_allow_html=True)
            
            full_name = st.text_input("Your Name", placeholder="Your Name")
            email = st.text_input("Your Email", placeholder="Your Email")
            password = st.text_input("Password", type="password", placeholder="Password")
            
            # Sub-row 1: Phone & Country side-by-side
            sub_col1, sub_col2 = st.columns(2, gap="medium")
            with sub_col1:
                phone = st.text_input("Phone Number", placeholder="Phone Number")
            with sub_col2:
                default_country_idx = COUNTRIES.index("Jordan") if "Jordan" in COUNTRIES else 0
                country = st.selectbox("Country", COUNTRIES, index=default_country_idx)

            # Sub-row 2: Gender & Date of Birth side-by-side
            sub_col3, sub_col4 = st.columns(2, gap="medium")
            with sub_col3:
                gender = st.selectbox("Gender", GENDERS)
            with sub_col4:
                date_of_birth = st.date_input(
                    "Date of Birth",
                    min_value=datetime.date(1940, 1, 1),
                    max_value=datetime.date.today()
                )

            submit_button = st.form_submit_button("Register")

        with col_right:
            st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
            st.image(
                "https://colorlib.com/etc/regform/colorlib-regform-7/images/signup-image.jpg",
                use_container_width=True
            )
            st.markdown(
                "<div style='text-align: center; margin-top: 30px;'>"
                "<a href='#' style='color: #222222; text-decoration: underline; font-size: 14px; font-weight: 400;'>I am already member</a>"
                "</div>",
                unsafe_allow_html=True
            )

    if submit_button:
        if not full_name or not email or not password or not phone:
            st.error("Please fill in all required fields.")
            return

        new_user = User(
            full_name=full_name,
            email=email,
            password=password,
            phone=phone,
            gender=gender.lower(),
            date_of_birth=str(date_of_birth),
            country=country
        )

        result = repo.create_user(new_user)

        if result.get("status") == "success":
            st.success(f"Account created successfully for {result.get('full_name')}!")
        else:
            st.error(f"Sign Up failed: {result.get('message')}")