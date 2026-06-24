import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="CivicGuardian AI",
    page_icon="🛡️"
)

st.title("🛡️ CivicGuardian AI")

if st.button("Test Gemini"):

    response = model.generate_content(
        "Say hello to CivicGuardian AI."
    )

    st.success(response.text)