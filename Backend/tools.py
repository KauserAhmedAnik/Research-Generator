"""
tools.py

Built-in CrewAI tools used by the agents.

Compatible with the latest CrewAI + crewai-tools.
"""

from crewai_tools import (
    TavilySearchTool,
    TavilyExtractorTool,
)




def get_search_tool() -> TavilySearchTool:
    """
    Returns the Tavily web search tool.

    Used by the Research Agent.
    """

    return TavilySearchTool(
        search_depth="advanced",
        max_results=8,
        include_answer=True,
        include_raw_content=True,
        include_images=False,
    )


def get_extractor_tool() -> TavilyExtractorTool:
    """
    Returns the webpage extraction tool.

    Used when the Research Agent needs
    to extract full content from URLs.
    """

    return TavilyExtractorTool(
        extract_depth="advanced",
        include_images=False,
    )