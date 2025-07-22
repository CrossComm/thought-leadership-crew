from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool

@CrewBase
class ThoughtLeadershipCrew():
    """Thought Leadership crew"""

    @agent
    def news_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['news_collector'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )

    @agent
    def strategic_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_analyst'],
            tools=[SerperDevTool()],
        )

    @agent
    def content_curator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_curator'],
            tools=[SerperDevTool()],
        )

    @agent
    def social_media_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_specialist'],
            tools=[SerperDevTool()],
        )


    @task
    def gather_news_from_trusted_sources(self) -> Task:
        return Task(
            config=self.tasks_config['gather_news_from_trusted_sources'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def supplement_with_additional_context(self) -> Task:
        return Task(
            config=self.tasks_config['supplement_with_additional_context'],
            tools=[SerperDevTool()],
        )

    @task
    def evaluate_strategic_importance(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_strategic_importance'],
            tools=[SerperDevTool()],
        )

    @task
    def select_most_important_stories(self) -> Task:
        return Task(
            config=self.tasks_config['select_most_important_stories'],
            tools=[SerperDevTool()],
        )

    @task
    def create_comprehensive_summaries(self) -> Task:
        return Task(
            config=self.tasks_config['create_comprehensive_summaries'],
            tools=[SerperDevTool()],
        )

    @task
    def identify_strategic_takeaways(self) -> Task:
        return Task(
            config=self.tasks_config['identify_strategic_takeaways'],
            tools=[SerperDevTool()],
        )

    @task
    def generate_social_media_content(self) -> Task:
        return Task(
            config=self.tasks_config['generate_social_media_content'],
            tools=[SerperDevTool()],
        )

    @task
    def compile_final_digest(self) -> Task:
        return Task(
            config=self.tasks_config['compile_final_digest'],
            tools=[SerperDevTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Thought Leadership crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
