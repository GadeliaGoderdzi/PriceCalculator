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

# Initialize an empty list to store user inputs and results
user_inputs = []
total_cost = 0  # Variable to accumulate the total cost

# Loop over each row in the CSV to ask the user how many they have
for index, row in data.iterrows():
    description = row['Fee']  # Fee is now a description
    rate = row['Rate']  # Rate is the actual rate
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

    # Display the total cost
    st.write(f"### Total Cost: ${total_cost}")

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


