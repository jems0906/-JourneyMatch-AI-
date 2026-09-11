from app.recommender.explainer import explain


def test_explain_lists_dimensions_at_or_above_threshold():
    breakdown = {"budget": 95, "climate": 88, "interests": 92, "accessibility": 100}
    explanation = explain(breakdown)
    assert "budget" in explanation and "climate" in explanation and "interests" in explanation and "accessibility" in explanation


def test_explain_falls_back_when_nothing_matches_well():
    breakdown = {"budget": 20, "climate": 10, "interests": 5, "accessibility": 0}
    assert explain(breakdown) == "a balanced mix of your trip preferences"
