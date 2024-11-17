import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Welcome Page",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set page background color to rich burgundy
st.markdown("""
<style>
body {
    background-color: #2B5288; /* Rich Burgundy */
    color: #FFFCEF; /* Ivory Cream */
    font-family: sans-serif;
}

.stButton {
    background-color: #FFFCEF;
    color: #2B5288;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
}

.stSidebar {
    background-color: #2B5288;
    color: #FFFCEF;
}
</style>
""", unsafe_allow_html=True)

def home_page():
    st.title("Hello, Welcome to Our Webpage")

    st.sidebar.header("Navigation")
    home_button = st.sidebar.button("Home")
    settings_button = st.sidebar.button("Settings")
    login_button = st.sidebar.button("Login")
    account_button = st.sidebar.button("Account")

    # Button functionality
    if home_button:
        st.write("Home button clicked!")
        # Add your desired actions for the Home button here
    if settings_button:
        st.write("Settings button clicked!")
        # Add your desired actions for the Settings button here
    if login_button:
        st.write("Login button clicked!")
        # Add your desired actions for the Login button here
    if account_button:
        st.write("Account button clicked!")
        # Add your desired actions for the Account button here

    # Embed QuickSight dashboard (replace with your actual QuickSight embed code)
    st.components.v1.iframe("https://your-quicksight-dashboard-embed-link")

def dashboard_page():
    # Embed QuickSight dashboard (replace with your actual QuickSight embed code)
    st.components.v1.iframe("https://your-quicksight-dashboard-embed-link")

# Main app logic
page = st.sidebar.radio("Navigation", ["Home", "Dashboard"], key="page_radio")

if page == "Home":
    home_page()
elif page == "Dashboard":
    dashboard_page()