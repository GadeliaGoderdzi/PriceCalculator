import streamlit as st
import pandas as pd


# Load the CSV file
@st.cache
def load_data():
    url = 'CSV/Container tariffs.csv'  # Replace with your CSV file URL or local path
    return pd.read_csv(url)


# Function to calculate cost based on input
def calculate_cost(rate, quantity):
    return rate * quantity


# Load the dataset
data = load_data()

# Initialize variables
total_quantity = 0  # To sum the quantities
first_rate = data.iloc[0]['Rate']  # Get the rate from the first row
user_inputs = []  # List to store user inputs
non_zero_costs = 0  # To accumulate non-zero costs

# Loop over each row, skipping the first one
for index, row in data.iloc[1:].iterrows():  # Skip the first row
    description = row['Fee']  # Fee is the des
