import streamlit as st
from datetime import datetime

# Class Definition
class Employee:
    def __init__(self, name, Tname):
        self.name = name
        self.Tname = Tname
        self.sales = 0
        self.salary = 0
        self.advance = 0

# Helper Functions
def calculate_total_cash(denominations):
    return sum(int(count) * int(value) for value, count in denominations.items())

def calculate_totals(employees, other_expenses):
    total_profit = sum(employee.sales for employee in employees)
    total_expenses = sum(employee.advance for employee in employees) + other_expenses
    return total_profit, total_expenses

# CSS Styles
st.markdown("""
    <style>
    .big-font { font-size:20px !important; font-weight: bold; }
    .blue-box { background-color: #FFCA3A; color: black; font-weight: bold; padding: 5px; }
    .green-box { background-color: #8AC926; color: black; font-weight: bold; padding: 5px; }
    .red-box { background-color: #FF595E; color: black; font-weight: bold; padding: 5px; }
    .yellow-box { background-color: #FF3300; font-weight: bold; padding: 5px; }
    div[class*="stDateInput"] label, div[class*="stNumberInput"] label {
        font-size: 50px; font-weight: bold; color: black; padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Application Title
st.title("Elite Salon Accounts")

# Employee Initialization
employees = [Employee("Ganesh", "கணேஷ்"), Employee("Siva", "சிவா"), 
             Employee("Jai", "ஜெய்"), Employee("Raja", "ராஜா")]

# Form for Input
with st.form("DailyAccounts_Form"):
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

    # Column 1: Daily Input
    with col1:
        st.markdown("<p class='big-font blue-box'>Daily Input</p>", unsafe_allow_html=True)
        date = st.date_input("Date", datetime.now())
        opening_cash = st.number_input("Opening Cash", min_value=0)
        # Disabled fields
        purchase_shop = st.number_input("Purchase Shop", min_value=0, disabled=True)
        total_sales_pos = st.number_input("Total Sales POS", min_value=0)
        paytm = st.number_input("Paytm", min_value=0)
        cash_withdrawn = st.number_input("Cash Withdrawn", min_value=0)
        cash_Difference = st.number_input("Cash Difference", min_value=0, disabled=True)

    # Column 2: Denominations
    with col2:
        st.markdown("<p class='big-font green-box'>Denominations</p>", unsafe_allow_html=True)
        denominations = {
            str(denom): st.number_input(f"₹{denom} x", min_value=0) for denom in [500, 200, 100, 50, 20, 10, 5, 2, 1]
        }
        total_cash = calculate_total_cash(denominations)
        st.number_input("Total: ", min_value=0, value=total_cash, disabled=True)

    # Column 3: Sales
    with col3:
        st.markdown("<p class='big-font red-box'>Sales</p>", unsafe_allow_html=True)
        for employee in employees:
            employee.sales = st.number_input(f"{employee.name} Sales", key=f"{employee.name}_Sales", min_value=0)
            # Disabled Salary Input
        for employee in employees:
            employee.salary = st.number_input(f"{employee.Tname} Salary", key=f"{employee.name}_Salary", min_value=0, disabled=True)

    # Column 4: Expenses
    with col4:
        st.markdown("<p class='big-font yellow-box'>Expenses</p>", unsafe_allow_html=True)
        for employee in employees:
            employee.advance = st.number_input(f"{employee.name} Advance", key=f"{employee.name}_Advance", min_value=0)
        cleaning, tea_snacks, food, other_expenses = (st.number_input(label, min_value=0) for label in 
                                                      ['House Keeping(Sudakar)', 'Tea & Snacks', 'Food', 'Other Expenses'])
        other_expense_name = st.selectbox("What Other Expense?", ["Other Expenses", "Flower", "News Paper", "Corporation Cleaning"])
        total_daily_expense = cleaning + tea_snacks + food + other_expenses + sum(employee.advance for employee in employees)
        st.number_input("Total Expense: ", min_value=0, value=total_daily_expense, disabled=True)
    
    # Submit Button
    submitted = st.form_submit_button("Save")
    if submitted:
        st.success("Data Saved Successfully!")
        #st.balloons()
        st.markdown("## Save Data")
        st.write("Date:", date.strftime("%Y-%m-%d"))
        st.write("Opening Cash:", opening_cash)
        st.write("Total Cash from Denominations:", total_cash)
        st.write("Total Expenses:", total_daily_expense)
        st.write("Purchase Shop", total_daily_expense)
