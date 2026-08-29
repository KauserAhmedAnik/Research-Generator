"""
pdf_generator.py

Converts Markdown reports into PDF.
"""

from pathlib import Path
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.units import inch


class PDFGenerator:
    """
    Generate PDF reports.
    """

    def __init__(self):

        self.styles = getSampleStyleSheet()

    def generate(
        self,
        topic: str,
        markdown: str,
        output_path: str,
    ):

        doc = SimpleDocTemplate(output_path)

        story = []

        title = Paragraph(
            f"<b>{topic}</b>",
            self.styles["Title"],
        )

        story.append(title)

        story.append(
            Spacer(
                1,
                0.3 * inch,
            )
        )

        date = Paragraph(
            datetime.now().strftime(
                "%d %B %Y %H:%M"
            ),
            self.styles["Normal"],
        )

        story.append(date)

        story.append(
            Spacer(
                1,
                0.4 * inch,
            )
        )

        for line in markdown.split("\n"):

            line = line.strip()

            if not line:

                story.append(
                    Spacer(
                        1,
                        0.15 * inch,
                    )
                )

                continue

            if line.startswith("# "):

                story.append(
                    Paragraph(
                        line[2:],
                        self.styles["Heading1"],
                    )
                )

            elif line.startswith("## "):

                story.append(
                    Paragraph(
                        line[3:],
                        self.styles["Heading2"],
                    )
                )

            elif line.startswith("### "):

                story.append(
                    Paragraph(
                        line[4:],
                        self.styles["Heading3"],
                    )
                )

            else:

                story.append(
                    Paragraph(
                        line,
                        self.styles["BodyText"],
                    )
                )

        doc.build(story)

        return Path(output_path)