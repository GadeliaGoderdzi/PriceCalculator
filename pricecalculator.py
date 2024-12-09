import streamlit as st
import pandas as pd

# Load the dataset from GitHub
url = 'https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/main/data.csv'
df = pd.read_csv(url)

# Streamlit App Title
st.title("Cargo Rate Calculator")

# Cargo Type Selection
cargo_type = st.selectbox(
    "Select your cargo type:", 
    df['cargo_type'].tolist()
)

# Metric Ton Input
metric_ton = st.number_input(
    "Enter the weight of your cargo in metric tons:", 
    min_value=0.0, 
    step=0.1
)

# Calculate Total Rate
if cargo_type and metric_ton > 0:
    rate = df[df['cargo_type'] == cargo_type]['rate'].values[0]
    total_cost = rate * metric_ton

    # Display Result
    st.subheader(f"Calculation Result:")
    st.write(f"**Cargo Type:** {cargo_type}")
    st.write(f"**Weight:** {metric_ton} metric tons")
    st.write(f"**Rate per Metric Ton:** ${rate}")
    st.write(f"**Total Cost:** ${total_cost:,.2f}")
else:
    st.info("Please select a cargo type and enter a valid weight.")
