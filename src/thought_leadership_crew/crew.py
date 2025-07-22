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
    def collect_and_enrich_news(self) -> Task:
        return Task(
            config=self.tasks_config['collect_and_enrich_news'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )

    @task
    def analyze_and_select_stories(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_and_select_stories'],
            tools=[SerperDevTool()],
        )

    @task
    def create_content_with_insights(self) -> Task:
        return Task(
            config=self.tasks_config['create_content_with_insights'],
            tools=[SerperDevTool()],
        )

    @task
    def generate_social_and_compile(self) -> Task:
        return Task(
            config=self.tasks_config['generate_social_and_compile'],
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