from dataclasses import dataclass


@dataclass(frozen=True)
class Recommendation:
    city: str
    country: str
    score: int
    explanation: str
