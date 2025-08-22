from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class NewsItem(BaseModel):
    """Individual news item with comprehensive information"""
    headline: str
    publication_date: str
    brief_description: str
    full_url: str
    background_info: Optional[str] = None
    related_developments: Optional[str] = None

class NewsItems(BaseModel):
    """Collection of news items from the news collector task"""
    items: List[NewsItem]
    total_count: Optional[int] = None

class RankedNewsItem(NewsItem):
    """News item with strategic ranking and analysis"""
    strategic_score: float  # 1-10 scale composite score
    relevance_score: float  # How relevant to user_role
    impact_score: float     # Business impact potential
    feasibility_score: float # Implementation feasibility
    timeliness_score: float # Urgency and timing
    ranking_rationale: str  # Why this ranking was assigned
    strategic_takeaways: List[str]  # 2-3 key actionable insights
    priority: str  # high/medium/low

class RankedNewsAnalysis(BaseModel):
    """Output from strategic analysis and ranking"""
    user_role: str
    user_objective: str
    analysis_timestamp: str
    top_stories: List[RankedNewsItem]  # Top 5-10 stories
    total_analyzed: int
    ranking_methodology: str