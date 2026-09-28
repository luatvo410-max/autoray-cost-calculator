import streamlit as st

st.title("AutoRAY Vehicle Cost Calculator")
st.write("Estimate what a vehicle costs over the years you own it.")

car_price = st.number_input("Vehicle price ($)", min_value=0.0, value=20000.0, step=500.0)
years = st.number_input("Years you plan to own it", min_value=1, value=5, step=1)
gas_per_year = st.number_input("Gas cost per year ($)", min_value=0.0, value=2000.0, step=100.0)
maintenance_per_year = st.number_input("Maintenance cost per year ($)", min_value=0.0, value=800.0, step=100.0)
insurance_per_year = st.number_input("Insurance cost per year ($)", min_value=0.0, value=1200.0, step=100.0)

gas_total = gas_per_year * years
maintenance_total = maintenance_per_year * years
insurance_total = insurance_per_year * years
operating_cost = gas_total + maintenance_total + insurance_total
total_cost = car_price + operating_cost
average_per_year = total_cost / years

st.subheader("Your cost report")
st.write(f"Gas over {years} years: ${gas_total:,.2f}")
st.write(f"Maintenance over {years} years: ${maintenance_total:,.2f}")
st.write(f"Insurance over {years} years: ${insurance_total:,.2f}")
st.write(f"Operating costs: ${operating_cost:,.2f}")
st.write(f"Total ownership cost: ${total_cost:,.2f}")
st.write(f"Average cost per year: ${average_per_year:,.2f}")
st.caption("Simple estimate. It does not include financing, taxes, resale value, or depreciation.")

