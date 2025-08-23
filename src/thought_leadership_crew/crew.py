from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, output_json, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool
from crewai_tools import FileReadTool
from .config.llm_config import get_llm
from .output_classes import NewsItems, RankedNewsItem, RankedNewsAnalysis

@CrewBase
class ThoughtLeadershipCrew():
    """Thought Leadership crew"""
    
    def __init__(self):
        super().__init__()
        self.llm = get_llm()

#Agents
    @agent
    def news_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['news_collector'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def strategic_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_analyst'],
            tools=[SerperDevTool()],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def digest_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['digest_creator'],
            llm=self.llm,
            reasoning=True,
            max_reasoning_attempts=3,
            verbose=True,
        )

#Tasks
    @task
    def collect_and_enrich_news(self) -> Task:
        return Task(
            config=self.tasks_config['collect_and_enrich_news'],
            agent=self.news_collector(),
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
            output_pydantic=NewsItems,
            output_file='news_collector_output.json'
        )

    @task
    def analyze_and_select_stories(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_and_select_stories'],
            agent=self.strategic_analyst(),
            context=[self.collect_and_enrich_news()],
            tools=[SerperDevTool()],
            output_pydantic=RankedNewsAnalysis,
            output_file='analyze_and_select_stories_output.json',
        )    

    @task
    def create_executive_digest(self) -> Task:
        return Task(
            config=self.tasks_config['create_executive_digest'],
            agent=self.digest_creator(),
            context=[self.analyze_and_select_stories()],
            markdown=True,
            output_file='executive_digest.md',
            async_execution=True,
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