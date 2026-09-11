from app.recommender.scoring_model import _score
from app.destinations import DESTINATIONS


def _destination_by_city(city: str):
    return next(destination for destination in DESTINATIONS if destination.city == city)


def test_matching_climate_and_interests_scores_higher_than_mismatched():
    destination = _destination_by_city("Cancun")
    matching_score, matching_breakdown = _score(destination, {"budget": 1750, "climate": "warm", "interests": ["beach", "food"], "accessibility": True})
    mismatched_score, mismatched_breakdown = _score(destination, {"budget": 1750, "climate": "cold", "interests": ["nightlife"], "accessibility": True})
    assert matching_score > mismatched_score
    assert matching_breakdown["climate"] == 100
    assert mismatched_breakdown["climate"] < matching_breakdown["climate"]


def test_accessibility_requirement_penalizes_inaccessible_destination():
    inaccessible = _destination_by_city("Cape Town")
    score, breakdown = _score(inaccessible, {"budget": 2050, "accessibility": True})
    assert breakdown["accessibility"] < 50
    assert 0.0 <= score <= 1.0


def test_no_preferences_still_returns_a_bounded_score():
    destination = _destination_by_city("Lisbon")
    score, breakdown = _score(destination, {})
    assert 0.0 <= score <= 1.0
    assert breakdown["interests"] == 65
