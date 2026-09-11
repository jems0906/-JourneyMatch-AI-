from .preference_extractor import INTERESTS


def classify_interests(text: str) -> list[str]:
    normalized = text.lower()
    return [interest for interest in INTERESTS if interest in normalized]
