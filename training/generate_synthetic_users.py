from pathlib import Path
import csv
import random

INTERESTS = ("food", "culture", "nature", "adventure", "history", "nightlife", "relaxation", "beach")


def generate(count: int = 500, seed: int = 7) -> list[dict]:
    random.seed(seed)
    rows = []
    for index in range(count):
        interests = random.sample(INTERESTS, k=2 + index % 3)
        rows.append({"user_id": f"synthetic-{index:04d}", "budget": random.randrange(1200, 3501, 100), "climate": random.choice(("warm", "mild", "cold")), "interests": "|".join(interests), "accessibility": random.choice(("true", "false"))})
    return rows


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "data_samples" / "synthetic_users.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        rows = generate()
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} synthetic users to {output}")
