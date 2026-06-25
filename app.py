import streamlit as st

from agents.coordinator import CoordinatorAgent
from agents.document_agent import DocumentAgent
from agents.planner_agent import PlannerAgent
from agents.report_agent import ReportAgent


# Initialize Agents
agent = CoordinatorAgent()
document_agent = DocumentAgent()
planner_agent = PlannerAgent()
report_agent = ReportAgent()

uploaded_docs = []

# Page Configuration
st.set_page_config(
    page_title="CivicGuardian AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CivicGuardian AI")
st.subheader("Your Personal Government Case Worker")

# User Inputs
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
    min_value=0,
    value=20000
)

# PDF Upload
uploaded_file = st.file_uploader(
    "Upload Supporting Document (PDF)",
    type=["pdf"]
)

# Process PDF
if uploaded_file is not None:

    try:

        text = document_agent.read_pdf(
            uploaded_file
        )

        uploaded_docs = (
            document_agent.detect_documents(
                text
            )
        )

        st.success(
            "Document uploaded successfully!"
        )

        st.write(
            "### Detected Documents"
        )

        st.write(uploaded_docs)

    except Exception as e:

        st.error(
            f"Could not process PDF: {e}"
        )

# Main Button
if st.button("Find Schemes"):

    try:

        result = agent.process(
        occupation,
        income
        )

        st.write(
        "## Recommended Schemes"
        )

        st.write(
        result["explanation"]
        )

        required_docs = [
            "Aadhaar",
            "Income Certificate"
        ]

        plan = planner_agent.create_plan(
            required_docs,
            uploaded_docs
        )

        st.write(plan)

        pdf_content = (
        result["explanation"]
        + "\n\n"
        + plan
        )

        pdf_file = (
            report_agent.generate_pdf(
                pdf_content
            )
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Report",
                data=file,
                file_name="CivicGuardian_Report.pdf",
                mime="application/pdf"
            )

    except Exception as e:

        st.error(
            f"Error generating recommendations: {e}"
        )