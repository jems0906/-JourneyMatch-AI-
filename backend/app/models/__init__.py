"""Domain and persistence models."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Destination:
	city: str
	country: str
	airport: str
	climate: str
	avg_cost: int
	accessibility: bool
	interests: tuple[str, ...]
	description: str
	highlights: tuple[str, ...]


@dataclass
class Session:
	session_id: str
	preferences: dict[str, Any] = field(default_factory=dict)
	recommendation_count: int = 0
	feedback: list[int] = field(default_factory=list)
