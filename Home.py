# import libraries
import streamlit as st
import requests


# Set page
st.set_page_config(
    page_title="Astro Mind🌌",
    page_icon="🌌",
)
st.title("Astro Mind🌌")
st.subheader("Hi there ")
st.sidebar.success("Select a page above Dude")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
