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

# Loop over each row, skipping the first one
for index, row in data.iloc[1:].iterrows():  # Skip the first row
    description = row['Fee']  # Fee is the description
    rate = row['Rate']  # Rate from each row (not used directly for calculation)
    # Ask the user how many containers they have
    quantity = st.number_input(f"How many {description} containers do you have?", min_value=0, step=1)

    # Add the input quantity to the total quantity
    total_quantity += quantity

    # Store the user input for later analysis
    user_inputs.append({
        'Description': description,
        'Rate': rate,
        'Quantity': quantity,
        'Calculated Cost': calculate_cost(rate, quantity)
    })

# Calculate the total cost by multiplying the total quantity with the first rate value
total_cost = calculate_cost(first_rate, total_quantity)

# Display the detailed calculation before the "Save my input" button
if user_inputs:
    st.write("### Detailed Calculations:")

    # Create a DataFrame for the detailed calculations
    calculation_df = pd.DataFrame(user_inputs)

    # Display each row with a formatted calculation
    for idx, row in calculation_df.iterrows():
        description = row['Description']
        quantity = row['Quantity']
        rate = row['Rate']
        calculated_cost = row['Calculated Cost']
        st.write(f"For {description}: {quantity} x {rate} = ${calculated_cost}")

    # Display the total cost
    st.write(f"### Total Cost (Total Quantity x Rate from first row): ${total_cost}")

# Button to save user input to a CSV file
# Save to CSV and allow download
if st.button("Save my inputs"):
    user_inputs_df = pd.DataFrame(user_inputs)
    
    # Convert dataframe to CSV and create a download link
    csv_data = user_inputs_df.to_csv(index=False)
    st.download_button(
        label="Download your input data",
        data=csv_data,
        file_name="user_inputs.csv",
        mime="text/csv"
    )
    st.write("Your inputs are ready for download!")
