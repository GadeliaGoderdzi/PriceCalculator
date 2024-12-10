import streamlit as st

# Define the main function for each page
def page_1():
    st.title("Page 1")
    st.write("This is page 1")

def page_2():
    st.title("Page 2")
    st.write("This is page 2")

def page_3():
    st.title("Page 3")
    st.write("This is page 3")


# Create a radio button or selectbox in the sidebar to switch between pages
page = st.sidebar.radio("Select a page", ["Page 1", "Page 2", "Page 3"])


# Call the function for the selected page
if page == "Page 1":
    page_1()
elif page == "Page 2":
    page_2()
else:
    page_3()
