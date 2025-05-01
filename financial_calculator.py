
import streamlit as st
import math

# Constants
INTEREST_RATE = 8 / 100  # 8%
MONTHS = 12

st.set_page_config(page_title="Financial Calculator", layout="centered")

st.title("💰 Financial Calculator")
st.write("Choose an option below to calculate your financial values:")

# Sidebar Navigation
option = st.sidebar.radio("Select Calculator", ["Investment", "Bond"])

if option == "Investment":
    st.header("📈 Investment Calculator")
    st.write("""
        This calculator helps you determine the return on your investment over **12 months**,
        using either **simple** or **compound interest**.
        Interest rate is fixed at **8% annually**.
    """)

    deposit = st.number_input("Enter your deposit amount (R)", min_value=0.0, value=1000.0)
    interest_type = st.radio("Select interest type", ["Simple", "Compound"])

    if st.button("Calculate Investment"):
        years = MONTHS / 12
        if interest_type == "Simple":
            # Simple interest formula: A = P(1 + rt)
            amount = deposit * (1 + INTEREST_RATE * years)
            st.code(f"A = P(1 + rt) = {deposit} * (1 + {INTEREST_RATE} * {years})")
        else:
            # Compound interest formula: A = P(1 + r)^t
            amount = deposit * math.pow((1 + INTEREST_RATE), years)
            st.code(f"A = P(1 + r)^t = {deposit} * (1 + {INTEREST_RATE})^{years}")

        st.success(f"💸 Your investment will be worth: **R{round(amount, 2)}** after 12 months.")

elif option == "Bond":
    st.header("🏠 Bond Calculator")
    st.write("""
        This calculator determines the **monthly repayment** on a house loan over **12 months**.
        The interest rate is fixed at **8% annually**.
    """)

    house_value = st.number_input("Enter the present value of the house (R)", min_value=0.0, value=250000.0)

    if st.button("Calculate Bond"):
        i = INTEREST_RATE / 12
        n = MONTHS

        # Bond repayment formula: (i * P) / (1 - (1 + i)^-n)
        repayment = (i * house_value) / (1 - math.pow((1 + i), -n))
        st.code(f"Repayment = (i * P) / (1 - (1 + i)^-n)\n= ({i:.4f} * {house_value}) / (1 - (1 + {i:.4f})^-{n})")

        st.success(f"📅 Your monthly repayment is: **R{round(repayment, 2)}**")
