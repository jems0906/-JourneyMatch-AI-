"""Recommendation package facade."""

from ..nlp.preference_extractor import extract_preferences
from .hybrid import recommend

__all__ = ["extract_preferences", "recommend"]
