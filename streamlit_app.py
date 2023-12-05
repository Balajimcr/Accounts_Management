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

# Initialize session state for denominations
if 'denominations' not in st.session_state:
    st.session_state['denominations'] = {str(denom): 0 for denom in [500, 200, 100, 50, 20, 10, 5, 2, 1]}

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

# Initialize session state for denominations
if 'denominations' not in st.session_state:
    st.session_state['denominations'] = {str(denom): 0 for denom in [500, 200, 100, 50, 20, 10, 5, 2, 1]}

# Form for Input
with st.form("DailyAccounts_Form"):
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

    # Column 1: Daily Input
    with col1:
        st.markdown("<p class='big-font blue-box'>Daily Input</p>", unsafe_allow_html=True)
        date = st.date_input("Date", datetime.now(),format="DD/MM/YYYY")
        opening_cash = st.number_input("Opening Cash", min_value=0,step=100)
        # Disabled fields        
        total_sales_pos = st.number_input("Total Sales POS", min_value=0,step=100)
        paytm = st.number_input("Paytm", min_value=0,step=100)
        cash_withdrawn = st.number_input("Cash Withdrawn", min_value=0,step=500)
        cash_Difference = st.number_input("Cash Difference", min_value=-100,value=0, disabled=True)

    # Column 2: Denominations
    with col2:
        st.markdown("<p class='big-font green-box'>Denominations</p>", unsafe_allow_html=True)
        for denom in [500, 200, 100, 50, 20, 10, 5, 2, 1]:
            denom_key = f"denom_{denom}"
            st.session_state['denominations'][str(denom)] = st.number_input(f"₹{denom} x", min_value=0, key=denom_key, value=st.session_state['denominations'][str(denom)])

        # Recalculate total cash each time the script runs
        total_cash = calculate_total_cash(st.session_state['denominations'])
        st.number_input("Total", min_value=0, value=total_cash, disabled=True)

    # Column 3: Sales
    with col3:
        st.markdown("<p class='big-font red-box'>Sales</p>", unsafe_allow_html=True)
        for employee in employees:
            employee.sales = st.number_input(f"{employee.name} Sales", key=f"{employee.name}_Sales", min_value=0,step=100)
            # Disabled Salary Input
        for employee in employees:
            employee.salary = st.number_input(f"{employee.name} Salary", key=f"{employee.name}_Salary", min_value=0, disabled=True)

    # Column 4: Expenses
    with col4:
        st.markdown("<p class='big-font yellow-box'>Expenses</p>", unsafe_allow_html=True)
        for employee in employees:
            employee.advance = st.number_input(f"{employee.name} Advance", key=f"{employee.name}_Advance", min_value=0,step=100)
        cleaning, tea_snacks, food, other_expenses = (st.number_input(label, min_value=0,step=50) for label in 
                                                      ['House Keeping(Sudakar)', 'Tea & Snacks', 'Food', 'Other Expenses'])
        other_expense_name = st.selectbox("What Other Expense?",options=["Other Expenses", "Flower", "News Paper", "Corporation Cleaning"],index=None,placeholder="Select an expense")
        total_daily_expense = cleaning + tea_snacks + food + other_expenses + sum(employee.advance for employee in employees)
        st.number_input("Total Expense", min_value=0, value=total_daily_expense, disabled=True)
    
    # Submit Button
    submitted = st.form_submit_button("Save")
    if submitted:
        # Check if 'Other Expenses' is non-zero and 'other_expense_name' is not selected
        if other_expenses > 0 and other_expense_name == None:
            st.error("Please select a valid expense name!")
        else:
            # Compute the Stats
            Cash_Sales = total_sales_pos - paytm
            Total_Cash_inRegister = opening_cash + Cash_Sales - total_daily_expense
            cash_Difference = Total_Cash_inRegister - total_cash
            closing_cash = total_cash - cash_withdrawn
            
            st.markdown("## Data Saved")
            st.write("Date:", date.strftime("%d-%b-%Y"))
            st.write("Opening Cash:", opening_cash)
            st.write("Total Cash:", Total_Cash_inRegister)
            st.write("Total Expenses:", total_daily_expense)
            st.write("Closing Cash:", closing_cash)
            st.write("Cash Difference:", cash_Difference)
            
            st.success("Data Saved Successfully!")
            #st.balloons()
            

