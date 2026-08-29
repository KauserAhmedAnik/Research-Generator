"""
config.py

Application configuration settings.
Loads environment variables from the .env file.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")





REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)


DATABASE_URL = f"sqlite:///{DATABASE_DIR / 'reports.db'}"



TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# ---------------------------------------------------
# FastAPI Settings
# ---------------------------------------------------

API_TITLE = "Multi-Agent Research & Report Writer"

API_DESCRIPTION = (
    "A CrewAI-powered research assistant that generates "
    "professional reports using multiple AI agents."
)

API_VERSION = "1.0.0"

# ---------------------------------------------------
# Report Settings
# ---------------------------------------------------

DEFAULT_REPORT_NAME = "research_report.pdf"

MAX_TOPIC_LENGTH = 250

# ---------------------------------------------------
# Logging
# ---------------------------------------------------

LOG_LEVEL = "INFO"