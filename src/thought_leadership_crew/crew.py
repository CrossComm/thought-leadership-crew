from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool

@CrewBase
class ThoughtLeadershipCrew():
    """Thought Leadership crew"""

    @agent
    def news_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['news_scraper'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )

    @agent
    def strategic_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_analyzer'],
            tools=[SerperDevTool()],
        )

    @agent
    def digest_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['digest_creator'],
            tools=[SerperDevTool()],
        )

    @agent
    def social_media_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_content_creator'],
            tools=[SerperDevTool()],
        )


    @task
    def scrape_news_articles(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_news_articles'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )

    @task
    def analyze_strategic_importance(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_strategic_importance'],
            tools=[SerperDevTool()],
        )

    @task
    def create_news_digest(self) -> Task:
        return Task(
            config=self.tasks_config['create_news_digest'],
            tools=[SerperDevTool()],
        )

    @task
    def draft_social_media_posts(self) -> Task:
        return Task(
            config=self.tasks_config['draft_social_media_posts'],
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
