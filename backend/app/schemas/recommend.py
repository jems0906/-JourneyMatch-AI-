from pydantic import BaseModel, Field


class RecommendationRequest(BaseModel):
    session_id: str
    prompt: str = Field(min_length=8, max_length=2000)


class FeedbackRequest(BaseModel):
    session_id: str
    rating: int = Field(ge=1, le=5)
    destination: str | None = None
    action: str = "rating"
