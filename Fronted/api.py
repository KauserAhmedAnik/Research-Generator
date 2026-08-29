
"""
api.py

Functions for communicating with FastAPI.
"""

import requests

from config import (
    GENERATE_ENDPOINT,
    REPORTS_ENDPOINT,
)


def generate_report(topic: str):
    """
    Generate a new report through FastAPI.
    """

    response = requests.post(
        GENERATE_ENDPOINT,
        json={
            "topic": topic
        },
        timeout=600,
    )

    response.raise_for_status()

    return response.json()


def get_reports():
    """
    Get all generated reports.
    """

    response = requests.get(
        REPORTS_ENDPOINT,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def delete_report(report_id: int):
    """
    Delete a report from the database.
    """

    response = requests.delete(
        f"{REPORTS_ENDPOINT}/{report_id}",
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def download_report(report_id: int):
    """
    Download the PDF file from FastAPI.
    """

    response = requests.get(
        f"{REPORTS_ENDPOINT}/{report_id}/download",
        timeout=60,
    )

    response.raise_for_status()

    return response.content

