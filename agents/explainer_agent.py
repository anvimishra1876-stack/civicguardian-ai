import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


class ExplainerAgent:

    def explain(
        self,
        occupation,
        income,
        schemes_text
    ):

        prompt = f"""
You are CivicGuardian AI.

User Profile:
Occupation: {occupation}
Income: {income}

Eligible Schemes:
{schemes_text}

Explain:

1. Why the user qualifies
2. Benefits of each scheme
3. Required documents
4. Next steps

Keep the response simple and friendly.
"""

        try:
            response = model.generate_content(prompt)
            return response.text

        except Exception:
            return schemes_text