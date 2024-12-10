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

# Initialize an empty list to store user inputs
user_inputs = []

# Loop over each row in the CSV to ask the user how many they have
for index, row in data.iterrows():
    fee = row['Fee']
    rate = row['Rate']
    description = row['Fee']

    # Ask the user how many containers they have
    quantity = st.number_input(f"How many {description} containers do you have?", min_value=0, step=1)

    # Calculate cost if quantity is entered
    if quantity > 0:
        cost = calculate_cost(rate, quantity)
        st.write(f"Total cost for {quantity} {description} containers: ${cost}")
    else:
        cost = 0
    
    # Store the user input for later analysis
    user_inputs.append({
        'Description': description,
        'Fee': fee,
        'Rate': rate,
        'Quantity': quantity,
        'Total Cost': cost
    })

    # Add this cost to the total
    total_cost += cost

# Display the total results before the "Save my input" button
if user_inputs:
    st.write("### Summary of Your Inputs and Costs:")
    results_df = pd.DataFrame(user_inputs)
    st.write(results_df)

    st.write(f"### Total Cost: ${total_cost}")





