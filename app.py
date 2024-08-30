# -*- coding:utf-8 -*-

import streamlit as st
from streamlit_option_menu import option_menu
from utils import load_eda_data
from survey import survey_display

# Page configuration
st.set_page_config(
    page_title="재무건강 상태 진단",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

def main():
    st.markdown("<h1 style='text-align: center;'> 🚑재무건강 상태 진단</h1>", unsafe_allow_html=True)

    st.markdown("""---""")
   
    survey_display()


if __name__ == "__main__":
    main()