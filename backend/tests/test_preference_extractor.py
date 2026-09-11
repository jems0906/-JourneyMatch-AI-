from app.nlp.preference_extractor import extract_preferences


def test_extract_preferences_parses_budget_climate_origin_and_interests():
    preferences = extract_preferences("Warm beach vacation, budget around $2,000, flying from ATL, love food and culture")
    assert preferences["budget"] == 2000
    assert preferences["climate"] == "warm"
    assert preferences["origin"] == "ATL"
    assert "food" in preferences["interests"] and "culture" in preferences["interests"]


def test_extract_preferences_defaults_when_fields_are_absent():
    preferences = extract_preferences("Just want to travel somewhere nice")
    assert preferences["budget"] == 2200
    assert preferences["climate"] is None
    assert preferences["accessibility"] is False
