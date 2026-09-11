from dataclasses import dataclass


@dataclass(frozen=True)
class Feedback:
    session_id: str
    rating: int
    destination: str | None = None
    action: str = "rating"
