import csv
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app.destinations import DESTINATIONS


if __name__ == "__main__":
    output = ROOT / "data_samples" / "destinations.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["city", "country", "airport", "climate", "avg_cost", "accessibility", "interests", "description"])
        for destination in DESTINATIONS:
            writer.writerow([destination.city, destination.country, destination.airport, destination.climate, destination.avg_cost, str(destination.accessibility).lower(), "|".join(destination.interests), destination.description])
    print(f"wrote {len(DESTINATIONS)} destinations to {output}")
