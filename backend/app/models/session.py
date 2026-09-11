from dataclasses import dataclass, field
from typing import Any


@dataclass
class Session:
    session_id: str
    preferences: dict[str, Any] = field(default_factory=dict)
    recommendation_count: int = 0
    feedback: list[int] = field(default_factory=list)
