"""
report_service.py

Business logic for generating and storing research reports.
"""

from pathlib import Path
from datetime import datetime

from sqlalchemy.orm import Session

from crew import generate_report
from models import Report
from utils.pdf_generator import PDFGenerator


class ReportService:
    """
    Handles report generation and persistence.
    """

    def __init__(self, db: Session):
        self.db = db

        BASE_DIR = Path(__file__).resolve().parent.parent
        self.report_dir = BASE_DIR / "reports"
        self.report_dir.mkdir(parents=True, exist_ok=True)

        self.pdf_generator = PDFGenerator()

    def generate(self, topic: str) -> Report:
        """
        Generate a research report using CrewAI,
        save it as Markdown and PDF, and store
        the information in the database.
        """

        start_time = datetime.now()

        # Run CrewAI
        crew_result = generate_report(topic)

        markdown = str(crew_result)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        # --------------------------------------------------
        # Save Markdown
        # --------------------------------------------------

        md_filename = f"report_{timestamp}.md"

        md_path = self.report_dir / md_filename

        md_path.write_text(
            markdown,
            encoding="utf-8"
        )

        # --------------------------------------------------
        # Generate PDF
        # --------------------------------------------------

        pdf_filename = f"report_{timestamp}.pdf"

        pdf_path = self.report_dir / pdf_filename

        self.pdf_generator.generate(
            topic=topic,
            markdown=markdown,
            output_path=str(pdf_path),
        )

        # --------------------------------------------------
        # Calculate generation time
        # --------------------------------------------------

        generation_time = (
            datetime.now() - start_time
        ).total_seconds()

        # --------------------------------------------------
        # Save database record
        # --------------------------------------------------

        report = Report(
            topic=topic,
            report=markdown,
            markdown_path=str(md_path),
            pdf_path=str(pdf_path),
            status="Completed",
            generation_time=generation_time,
        )

        self.db.add(report)

        self.db.commit()

        self.db.refresh(report)

        return report

    def get_all_reports(self):

        return (
            self.db.query(Report)
            .order_by(Report.created_at.desc())
            .all()
        )

    def get_report(self, report_id: int):

        return (
            self.db.query(Report)
            .filter(Report.id == report_id)
            .first()
        )

    def delete_report(self, report_id: int):

        report = self.get_report(report_id)

        if report is None:
            return False

        # Keep the Markdown and PDF files.
        # Only remove the database record.

        self.db.delete(report)

        self.db.commit()

        return True