"""
tasks.py

Task definitions for the Multi-Agent Research & Report Writer.
Compatible with CrewAI 1.15.x
"""

from crewai import Task

from agents import (
    research_agent,
    analyst_agent,
    writer_agent,
    editor_agent,
)


def create_research_task() -> Task:
    return Task(
        name="Research Task",
        description="""
Conduct comprehensive research on the topic:

{topic}

Instructions:

1. Search multiple reliable sources.
2. Collect recent information.
3. Include statistics where available.
4. Save source URLs.
5. Verify facts before using them.
6. Avoid duplicate information.
""",
        expected_output="""
A structured research document including:

- Executive Summary
- Key Findings
- Facts
- Statistics
- Source URLs
""",
        agent=research_agent,
        markdown=True,
    )


def create_analysis_task(research_task: Task) -> Task:
    return Task(
        name="Analysis Task",
        description="""
Analyze the research collected.

Responsibilities:

- Remove duplicate information.
- Compare sources.
- Identify trends.
- Identify contradictions.
- Organize information logically.
- Create a report outline.
""",
        expected_output="""
A structured outline containing:

- Main Sections
- Supporting Facts
- Important Insights
- Citation Mapping
""",
        context=[research_task],
        agent=analyst_agent,
        markdown=True,
    )


def create_writing_task(analysis_task: Task) -> Task:
    return Task(
        name="Writing Task",
        description="""
Write a professional research report.

Required sections:

# Title

## Executive Summary

## Introduction

## Background

## Main Discussion

## Key Findings

## Challenges

## Future Scope

## Conclusion

## References
""",
        expected_output="""
A complete research report in Markdown with proper headings,
citations, and references.
""",
        context=[analysis_task],
        agent=writer_agent,
        markdown=True,
    )


def create_editing_task(writing_task: Task) -> Task:
    return Task(
        name="Editing Task",
        description="""
Review the report.

Check:

- Grammar
- Clarity
- Formatting
- Logical flow
- References
- Citations
- Professional writing quality

Improve the report without removing useful content.
""",
        expected_output="""
A publication-ready Markdown report.
""",
        context=[writing_task],
        agent=editor_agent,
        markdown=True,
        output_file="reports/final_report.md",
    )