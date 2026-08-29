"""
schemas.py

Pydantic schemas for request and response validation.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReportCreate(BaseModel):
    """
    Request model for generating a report.
    """

    topic: str


class ReportResponse(BaseModel):
    """
    Response model returned by the API.
    """

    id: int

    topic: str

    report: str

    markdown_path: Optional[str] = None

    pdf_path: Optional[str] = None

    status: str

    generation_time: float

    created_at: datetime

    model_config = {
        "from_attributes": True
    }