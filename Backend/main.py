"""
app.py

Main FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from api.report import router as report_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Multi-Agent Research & Report Writer",
    description="AI-powered research report generator using CrewAI.",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routes
app.include_router(report_router)


@app.get("/")
def root():
    return {
        "message": "Multi-Agent Research & Report Writer API",
        "status": "Running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }