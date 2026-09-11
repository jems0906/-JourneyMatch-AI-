import re
from typing import Any


INTERESTS = ("food", "culture", "nature", "adventure", "history", "nightlife", "relaxation", "beach")
CLIMATES = ("warm", "mild", "cold")


def extract_preferences(text: str) -> dict[str, Any]:
	normalized = text.lower()
	interests = [interest for interest in INTERESTS if interest in normalized]
	climate = next((value for value in CLIMATES if value in normalized), None)
	budget_match = re.search(r"\$\s*([\d,]+)", normalized)
	duration_match = re.search(r"(\d+)\s*(?:day|night)", normalized)
	airport_match = re.search(r"\b([a-z]{3})\b", normalized)
	return {"budget": int(budget_match.group(1).replace(",", "")) if budget_match else 2200, "climate": climate, "origin": airport_match.group(1).upper() if airport_match else None, "interests": interests, "accessibility": any(term in normalized for term in ("wheelchair", "accessible", "mobility")), "duration": int(duration_match.group(1)) if duration_match else None}

__all__ = ["extract_preferences"]
