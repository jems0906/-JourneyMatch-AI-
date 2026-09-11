import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "backend"))

from app.recommender import recommend
try:
    from .data_loader import load_synthetic_users
except ImportError:
    from data_loader import load_synthetic_users


def evaluate(limit: int = 100) -> dict[str, float]:
    users = load_synthetic_users()[:limit]
    covered = 0
    for user in users:
        preferences = {"budget": int(user["budget"]), "climate": user["climate"], "interests": user["interests"].split("|"), "accessibility": user["accessibility"] == "true"}
        covered += bool(recommend(preferences))
    return {"users_evaluated": len(users), "recommendation_coverage": covered / len(users) if users else 0.0}


if __name__ == "__main__":
    print(evaluate())
