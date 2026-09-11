from app.recommender.content_based import content_similarity


def test_content_similarity_returns_ranked_results_within_limit():
    results = content_similarity({"budget": 1900, "climate": "mild", "interests": ["food", "culture"]}, limit=2)
    assert len(results) == 2
    assert results[0]["score"] >= results[1]["score"]
