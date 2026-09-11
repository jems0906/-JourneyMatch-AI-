def explain(breakdown: dict[str, int]) -> str:
    matched = [key for key in ("climate", "interests", "budget", "accessibility") if breakdown[key] >= 70]
    return ", ".join(matched) if matched else "a balanced mix of your trip preferences"
