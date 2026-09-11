from typing import Any

from .explainer import explain
from .scoring_model import rank_destinations


def recommend(preferences: dict[str, Any], limit: int = 3) -> list[dict[str, Any]]:
    results = []
    for item in rank_destinations(preferences, limit):
        destination = item["destination"]
        results.append({"city": destination.city, "country": destination.country, "airport": destination.airport, "description": destination.description, "highlights": destination.highlights, "avg_cost": destination.avg_cost, "score": round(item["score"] * 100), "breakdown": item["breakdown"], "explanation": f"Recommended because it matches your {explain(item['breakdown'])}.", "accessibility": destination.accessibility})
    return results
