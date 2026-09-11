from app.recommender import extract_preferences, recommend


def test_extracts_structured_preferences():
    preferences = extract_preferences("Warm beach vacation in December, budget around $2,000, flying from ATL, love food and culture, need wheelchair accessibility")
    assert preferences["budget"] == 2000
    assert preferences["origin"] == "ATL"
    assert preferences["accessibility"] is True
    assert "food" in preferences["interests"]


def test_recommendations_are_ranked_and_explainable():
    results = recommend({"budget": 1800, "climate": "warm", "interests": ["beach", "food"], "accessibility": True})
    assert len(results) == 3
    assert results[0]["score"] >= results[1]["score"]
    assert results[0]["breakdown"]["budget"] >= 0
    assert "Recommended because" in results[0]["explanation"]
