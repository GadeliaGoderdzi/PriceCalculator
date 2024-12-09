# Load the dataset from GitHub
url = 'containersexample1.csv'
df = pd.read_csv(url)

# Streamlit App Title
st.title("Cargo Move Rate Calculator")

# Store user inputs
total_cost = 0
user_inputs = {}

# Dynamic Questions Based on CSV
st.subheader("Enter the Quantities for Each Move Type:")

for index, row in df.iterrows():
    move_type = row['Load Discharge Move']
    rate = row['Rate']
    
    # Ask the user how many moves
    quantity = st.number_input(
        f"How many {move_type}?", 
        min_value=0, 
        step=1, 
        key=f"{move_type}_input"
    )
    
    # Store user input and calculate total
    user_inputs[move_type] = quantity
    total_cost += quantity * rate

# Display the Calculation Result
st.subheader("Calculation Result:")
if total_cost > 0:
    for move_type, quantity in user_inputs.items():
        if quantity > 0:
            rate = df[df['Load Discharge Move'] == move_type]['Rate'].values[0]
            st.write(f"**{move_type}:** {quantity} x ${rate} = ${quantity * rate}")
    
    st.write(f"**Total Cost:** ${total_cost:,.2f}")
else:
    st.info("Please enter at least one cargo quantity.")
