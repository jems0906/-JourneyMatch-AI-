import csv
from pathlib import Path


def load_synthetic_users(path: str | Path | None = None) -> list[dict]:
    source = Path(path or Path(__file__).parents[1] / "data_samples" / "synthetic_users.csv")
    if not source.exists():
        from .generate_synthetic_users import generate
        return generate()
    with source.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
