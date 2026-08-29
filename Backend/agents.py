"""
agents.py

Defines all CrewAI agents used in the project.

Compatible with:
- Latest CrewAI
- GitHub Models
"""

import os

from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

from tools import (
    get_search_tool,
    get_extractor_tool,
)



# ==========================================================
# LLM
# ==========================================================

llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0.2,
)


# ==========================================================
# Research Agent
# ==========================================================

research_agent = Agent(
    role="Senior Research Specialist",
    goal=(
        "Gather accurate, up-to-date and trustworthy "
        "information from the internet."
    ),
    backstory=(
        "You are an experienced internet researcher who "
        "collects reliable information from multiple sources. "
        "You always include source links and avoid unsupported claims."
    ),
    tools=[
        get_search_tool(),
        get_extractor_tool(),
    ],
    llm=llm,
    verbose=True,
    memory=False,
    allow_delegation=False,
)


# ==========================================================
# Analyst Agent
# ==========================================================

analyst_agent = Agent(
    role="Research Analyst",
    goal=(
        "Analyze research findings and organize them into "
        "a logical structure."
    ),
    backstory=(
        "You are an expert analyst. "
        "You identify key insights, remove duplicate information, "
        "compare sources, and prepare a structured outline."
    ),
    llm=llm,
    verbose=True,
    memory=False,
    allow_delegation=False,
)


# ==========================================================
# Writer Agent
# ==========================================================

writer_agent = Agent(
    role="Technical Report Writer",
    goal=(
        "Write professional research reports in clear "
        "academic language."
    ),
    backstory=(
        "You specialize in writing technical reports. "
        "Your reports include an executive summary, "
        "headings, tables when appropriate, and properly "
        "organized references."
    ),
    llm=llm,
    verbose=True,
    memory=False,
    allow_delegation=False,
)


# ==========================================================
# Editor Agent
# ==========================================================

editor_agent = Agent(
    role="Senior Editor",
    goal=(
        "Review reports for quality, correctness, grammar, "
        "clarity and citation consistency."
    ),
    backstory=(
        "You are the final reviewer before publication. "
        "You improve readability, fix formatting issues, "
        "verify logical flow and ensure references are present."
    ),
    llm=llm,
    verbose=True,
    memory=False,
    allow_delegation=False,
)