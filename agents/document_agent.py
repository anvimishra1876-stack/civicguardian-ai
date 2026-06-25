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

        documents = []

        keywords = {
            "Aadhaar": [
                "aadhaar",
                "aadhar",
                "uidai"
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

        for document, words in keywords.items():

            for word in words:

                if word in text:
                    documents.append(document)
                    break

        return documents