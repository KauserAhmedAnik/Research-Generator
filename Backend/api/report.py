"""
report.py

REST API endpoints for report generation.
"""
from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from database import get_db
from services.report_service import ReportService

from schemas import (
    ReportCreate,
    ReportResponse,
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.post(
    "/generate",
    response_model=ReportResponse,
)
def generate_report(
    request: ReportCreate,
    db: Session = Depends(get_db),
):
    """
    Generate a new research report.
    """

    service = ReportService(db)

    report = service.generate(
        request.topic
    )

    return report


@router.get(
    "/",
    response_model=list[ReportResponse],
)
def get_reports(
    db: Session = Depends(get_db),
):
    """
    Return all reports.
    """

    service = ReportService(db)

    return service.get_all_reports()


@router.get(
    "/{report_id}",
    response_model=ReportResponse,
)
def get_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    """
    Return a single report.
    """

    service = ReportService(db)

    report = service.get_report(
        report_id
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    return report


@router.get(
    "/{report_id}/download",
)
def download_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    """
    Download the generated PDF report.
    """

    service = ReportService(db)

    report = service.get_report(
        report_id
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    if not report.pdf_path:
        raise HTTPException(
            status_code=404,
            detail="PDF file not found.",
        )

    pdf_file = Path(report.pdf_path)

    if not pdf_file.exists():
        raise HTTPException(
            status_code=404,
            detail="PDF file does not exist.",
        )

    return FileResponse(
        path=str(pdf_file),
        media_type="application/pdf",
        filename=pdf_file.name,
    )


@router.delete(
    "/{report_id}",
)
def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    """
    Delete a report from the database.

    The Markdown and PDF files are kept.
    """

    service = ReportService(db)

    deleted = service.delete_report(
        report_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    return {
        "message": "Report deleted successfully."
    }