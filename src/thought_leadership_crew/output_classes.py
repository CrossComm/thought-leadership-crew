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