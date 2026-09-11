from typing import Any

from ..destinations import DESTINATIONS


def _score(destination, preferences: dict[str, Any]) -> tuple[float, dict[str, int]]:
    budget = preferences.get("budget", 2200)
    budget_fit = max(0.0, 1 - abs(destination.avg_cost - budget) / max(budget, 1))
    climate_fit = 1.0 if not preferences.get("climate") or preferences["climate"] == destination.climate else 0.35
    wanted = set(preferences.get("interests", []))
    interest_fit = len(wanted.intersection(destination.interests)) / len(wanted) if wanted else 0.65
    accessibility_fit = 1.0 if not preferences.get("accessibility") or destination.accessibility else 0.05
    distance_fit = 1.0 if preferences.get("origin") == destination.airport else 0.72 if preferences.get("origin") else 0.7
    breakdown = {"budget": round(budget_fit * 100), "climate": round(climate_fit * 100), "interests": round(interest_fit * 100), "accessibility": round(accessibility_fit * 100), "flight": round(distance_fit * 100)}
    return 0.28 * budget_fit + 0.22 * climate_fit + 0.28 * interest_fit + 0.14 * accessibility_fit + 0.08 * distance_fit, breakdown


def rank_destinations(preferences: dict[str, Any], limit: int = 3) -> list[dict[str, Any]]:
    ranked = []
    for destination in DESTINATIONS:
        score, breakdown = _score(destination, preferences)
        ranked.append({"destination": destination, "score": score, "breakdown": breakdown})
    return sorted(ranked, key=lambda item: item["score"], reverse=True)[:limit]
