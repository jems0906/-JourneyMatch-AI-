from .scoring_model import rank_destinations


def content_similarity(preferences: dict, limit: int = 3) -> list[dict]:
    """Content-based compatibility facade for the deterministic baseline."""
    return rank_destinations(preferences, limit)
