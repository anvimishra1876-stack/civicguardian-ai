import streamlit as st

from agents.coordinator import CoordinatorAgent

agent = CoordinatorAgent()

st.title("🛡 CivicGuardian AI")

occupation = st.selectbox(
    "Occupation",
    [
        "Student",
        "Farmer",
        "Entrepreneur",
        "Senior Citizen"
    ]
)

income = st.number_input(
    "Annual Income",
    min_value=0
)

if st.button("Find Schemes"):

    result = agent.process(
        occupation,
        income
    )

    st.write(result)