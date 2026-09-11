from collections import Counter


def cluster_preferences(events: list[dict], limit: int = 5) -> list[dict[str, int]]:
    counts = Counter(
        interest
        for event in events
        if event.get("type") == "recommendation"
        for interest in event.get("preferences", {}).get("interests", [])
    )
    return [{"name": name, "count": count} for name, count in counts.most_common(limit)]
