from collections import Counter


def summarize(events: list[dict], sessions: dict) -> dict:
    recommendations = [event for event in events if event["type"] == "recommendation"]
    ratings = [event["rating"] for event in events if event["type"] == "feedback" and "rating" in event]
    clicks = [event for event in events if event["type"] == "click"]
    saves = [event for event in events if event["type"] == "save"]
    requested = sum(len(event.get("destinations", [])) for event in recommendations)
    reused = sum(1 for event in recommendations if event.get("reused"))
    destinations = Counter(destination for event in recommendations for destination in event.get("destinations", []))
    interests = Counter(interest for event in recommendations for interest in event.get("preferences", {}).get("interests", []))
    return {
        "sessions": len(sessions), "recommendations": requested,
        "average_satisfaction": round(sum(ratings) / len(ratings), 1) if ratings else 0,
        "feedback_count": len(ratings), "click_rate": round(len(clicks) / requested, 3) if requested else 0,
        "save_rate": round(len(saves) / requested, 3) if requested else 0,
        "response_reuse_rate": round(reused / len(recommendations), 3) if recommendations else 0,
        "cold_start_rate": 1.0 if recommendations else 0,
        "top_interests": [{"name": name, "count": count} for name, count in interests.most_common(5)],
        "most_recommended": [{"name": name, "count": count} for name, count in destinations.most_common(5)],
    }
