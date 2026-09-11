from typing import Any

from pydantic import BaseModel


class QualityDashboard(BaseModel):
    sessions: int
    recommendations: int
    average_satisfaction: float
    feedback_count: int
    click_rate: float
    save_rate: float
    response_reuse_rate: float
    cold_start_rate: float
    top_interests: list[dict[str, Any]]
    most_recommended: list[dict[str, Any]]
