import fitz


class DocumentAgent:

    def read_pdf(self, uploaded_file):

        pdf = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text()

        return text.lower()

def detect_documents(self, text):

    text = text.lower()

    documents = []

    keywords = {
        "Aadhaar": [
            "aadhaar",
            "aadhar",
            "uidai",
            "AADHAAR"
        ],
        "Income Certificate": [
            "income certificate"
        ],
        "Marksheet": [
            "marksheet",
            "mark sheet"
        ],
        "Land Record": [
            "land record",
            "land ownership"
        ]
    }

    for doc, words in keywords.items():

        for word in words:

            if word in text:
                documents.append(doc)
                break

    return documents

