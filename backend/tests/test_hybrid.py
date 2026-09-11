from app.recommender.hybrid import recommend


def test_hybrid_recommend_returns_explainable_ranked_destinations():
    results = recommend({"budget": 1750, "climate": "warm", "interests": ["beach", "food"], "accessibility": True}, limit=3)
    assert len(results) == 3
    scores = [item["score"] for item in results]
    assert scores == sorted(scores, reverse=True)
    for item in results:
        assert "Recommended because" in item["explanation"]
        assert set(item["breakdown"]) == {"budget", "climate", "interests", "accessibility", "flight"}
