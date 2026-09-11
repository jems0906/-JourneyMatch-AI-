from collections import Counter
from math import sqrt


def tokenize(text: str) -> list[str]:
    return [token.strip(".,!?;:").lower() for token in text.split() if token.strip(".,!?;:")]


def tfidf_vector(text: str, vocabulary: list[str]) -> list[float]:
    counts = Counter(tokenize(text))
    return [counts.get(term, 0) / max(len(counts), 1) for term in vocabulary]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    denominator = sqrt(sum(value * value for value in left)) * sqrt(sum(value * value for value in right))
    return numerator / denominator if denominator else 0.0
