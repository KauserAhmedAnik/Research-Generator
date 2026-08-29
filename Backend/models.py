"""
models.py

SQLAlchemy database models.
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime

from database import Base


class Report(Base):
    """
    Database table for generated research reports.
    """

    __tablename__ = "reports"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User input
    topic = Column(String(255), nullable=False)

    # Generated report (Markdown)
    report = Column(Text, nullable=False)

    # Generated Markdown path
    markdown_path = Column(String(500), nullable=True)
    # Generated PDF path
    pdf_path = Column(String(500), nullable=True)

    # Report status
    # Examples:
    # Generating
    # Completed
    # Failed
    status = Column(String(50), default="Generating")

    # Generation time in seconds
    generation_time = Column(Float, default=0.0)

    # Creation timestamp
    created_at = Column(DateTime, default=datetime.utcnow)