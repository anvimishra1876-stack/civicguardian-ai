import streamlit as st

from agents.coordinator import CoordinatorAgent
from agents.document_agent import DocumentAgent

# Initialize Agents
agent = CoordinatorAgent()
document_agent = DocumentAgent()

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

# Main Button
if st.button("Find Schemes"):

    # Document Processing
    if uploaded_file is not None:

        try:
            text = document_agent.read_pdf(
                uploaded_file
            )

            docs = document_agent.detect_documents(
                text
            )

            st.success("Document uploaded successfully!")

            st.write("### Detected Documents")
            st.write(docs)

        except Exception as e:
            st.error(
                f"Could not process PDF: {e}"
            )

    # AI Recommendation
    try:

        result = agent.process(
            occupation,
            income
        )

        st.write("## Recommended Schemes")
        st.write(result)

    except Exception as e:

        st.error(
            f"Error generating recommendations: {e}"
        )