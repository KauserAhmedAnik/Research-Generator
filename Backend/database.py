"""
database.py

Creates the SQLite database connection using SQLAlchemy.
Provides a reusable database session for FastAPI.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

# --------------------------------------------------
# Database Engine
# --------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Required for SQLite
    echo=False
)

# --------------------------------------------------
# Session Factory
# --------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# --------------------------------------------------
# Base Class
# --------------------------------------------------

Base = declarative_base()

# --------------------------------------------------
# Dependency
# --------------------------------------------------

def get_db():
    """
    FastAPI dependency.

    Creates a database session,
    yields it,
    then closes it automatically.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()