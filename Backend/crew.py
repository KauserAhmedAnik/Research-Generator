"""
crew.py

CrewAI orchestration.
Compatible with CrewAI 1.15.x
"""

from crewai import Crew, Process

from agents import (
    research_agent,
    analyst_agent,
    writer_agent,
    editor_agent,
)

from tasks import (
    create_research_task,
    create_analysis_task,
    create_writing_task,
    create_editing_task,
)


class ResearchCrew:

    def build(self) -> Crew:

        research_task = create_research_task()

        analysis_task = create_analysis_task(
            research_task
        )

        writing_task = create_writing_task(
            analysis_task
        )

        editing_task = create_editing_task(
            writing_task
        )

        return Crew(
            agents=[
                research_agent,
                analyst_agent,
                writer_agent,
                editor_agent,
            ],
            tasks=[
                research_task,
                analysis_task,
                writing_task,
                editing_task,
            ],
            process=Process.sequential,
            verbose=True,
            memory=False,
        )

    def run(self, topic: str):

        crew = self.build()

        result = crew.kickoff(
            inputs={
                "topic": topic
            }
        )

        return result


research_crew = ResearchCrew()


def generate_report(topic: str):

    return research_crew.run(topic)