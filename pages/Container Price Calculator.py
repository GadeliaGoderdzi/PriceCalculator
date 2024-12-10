import streamlit as st
import pandas as pd


# Load the CSV file
@st.cache
def load_data():
    url = 'https://github.com/yourusername/yourrepo/raw/main/data.csv'  # Replace with your CSV file URL or local path
    return pd.read_csv(url)
