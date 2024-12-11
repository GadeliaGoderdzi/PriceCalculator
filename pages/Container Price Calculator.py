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
    description = row['Fee']  # Fee is the description
    rate = row['Rate']  # Rate from each row (not used directly for calculation)
    # Ask the user how many containers they have
    quantity = st.number_input(f"How many {description} containers do you have?", min_value=0, step=1)

    # Add the input quantity to the total quantity
    total_quantity += quantity

    # Store the user input for later analysis
    calculated_cost = calculate_cost(rate, quantity)
    
    # Only add the calculated cost to non_zero_costs if quantity is greater than 0
    if quantity > 0:
        non_zero_costs += calculated_cost

    user_inputs.append({
        'Description': description,
        'Rate': rate,
        'Quantity': quantity,
        'Calculated Cost': calculated_cost
    })

# Calculate the first total cost by multiplying the total quantity with the first rate value
first_calculated_cost = calculate_cost(first_rate, total_quantity)

# The final total cost is the sum of the first calculation and all non-zero calculations
final_total_cost = first_calculated_cost + non_zero_costs

# Display the detailed calculation before the "Save my input" button
if user_inputs:
    st.write("### Detailed Calculations:")

    # Always show the total calculation for all containers and the first rate
    st.write(f"Total containers: {total_quantity} x {first_rate} = ${first_calculated_cost}")

    # Create a DataFrame for the detailed calculations
    calculation_df = pd.DataFrame(user_inputs)

    # Display each row with a formatted calculation, excluding rows where Quantity is 0
    for idx, row in calculation_df.iterrows():
        description = row['Description']
        quantity = row['Quantity']
        rate = row['Rate']
        calculated_cost = row['Calculated Cost']

        # Only show if quantity is greater than 0
        if quantity > 0:
            st.write(f"For {description}: {quantity} x {rate} = ${calculated_cost}")

    # Display the final total cost
    st.write(f"### Final Total Cost: ${final_total_cost}")

# Button to save user input to a CSV file
# Save to CSV and allow download
if st.button("Save my inputs"):
    # Add the final total cost to the user inputs for the CSV download
    user_inputs.append({
        'Description': 'Final Total Cost',
        'Rate': '',
        'Quantity': '',
        'Calculated Cost': final_total_cost
    })
    
    user_inputs_df = pd.DataFrame(user_inputs)
    
    # Convert dataframe to CSV and create a download link
    csv_data = user_inputs_df.to_csv(index=False)
    st.download_button(
        label="Download your input data with calculations",
        data=csv_data,
        file_name="user_inputs_with_calculations.csv",
        mime="text/csv"
    )
    st.write("Your inputs with calculations are ready for download!")
