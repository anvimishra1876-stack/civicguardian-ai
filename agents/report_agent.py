from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class ReportAgent:

    def generate_pdf(
        self,
        text
    ):

        filename = (
            "civicguardian_report.pdf"
        )

        doc = SimpleDocTemplate(
            filename
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "CivicGuardian AI Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        content.append(
            Paragraph(
                text.replace(
                    "\n",
                    "<br/>"
                ),
                styles["BodyText"]
            )
        )

        doc.build(content)

        return filename