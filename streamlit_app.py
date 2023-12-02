import streamlit as st
import pandas as pd
from datetime import datetime

# Title of the application
st.title("Daily Sales Accounts - Shop")

# Form for input
with st.form("sales_form"):
    # Date input
    date = st.date_input("Date", datetime.now())
    opening_cash = st.number_input("Opening Cash", min_value=0.0, format='%f')
    
    # Purchase Inputs
    purchase_shop = st.number_input("Purchase Shop", min_value=0.0, format='%f')
    other_purchase = st.number_input("Other Purchase", min_value=0.0, format='%f')
    
    # Sales Inputs
    total_sales_pos = st.number_input("Total Sales POS", min_value=0.0, format='%f')
    paytm = st.number_input("Paytm", min_value=0.0, format='%f')
    cash_withdrawn = st.number_input("Cash Withdrawn", min_value=0.0, format='%f')
    
    # Denominations
    denominations = {
        "500": st.number_input("₹500 x", min_value=0),
        "200": st.number_input("₹200 x", min_value=0),
        "100": st.number_input("₹100 x", min_value=0),
        "50": st.number_input("₹50 x", min_value=0),
        "20": st.number_input("₹20 x", min_value=0),
        "10": st.number_input("₹10 x", min_value=0),
        "5": st.number_input("₹5 x", min_value=0),
        "2": st.number_input("₹2 x", min_value=0),
        "1": st.number_input("₹1 x", min_value=0),
    }
    
    # Employee Sales Data
    employee_sales = {
        "Ganesh கணேஷ்": st.number_input("Ganesh கணேஷ் Profit", format='%f'),
        "Raja": st.number_input("Raja Profit", format='%f'),
        "Siva": st.number_input("Siva Profit", format='%f'),
    }
    
    # Shop Purchase Account
    employee_purchases = {
        "Ganesh கணேஷ்": st.number_input("Ganesh கணேஷ் Purchase", format='%f'),
        "Raja": st.number_input("Raja Purchase", format='%f'),
        "Employee Temp Jai": st.number_input("Jai Purchase", format='%f'),
        # Add other employees similarly
    }

    # Submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Processing and storing the form data
        st.write("Data submitted for date:", date)
        # Additional processing can be added here

# Display the submitted data - you can also save this to a database or a file
if submitted:
    st.write("Opening Cash:", opening_cash)
    st.write("Total Sales POS:", total_sales_pos)
    # Display other data similarly
