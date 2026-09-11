"""Placeholder for a future PostgreSQL seed; the demo currently uses curated in-memory data."""

from app.destinations import DESTINATIONS


if __name__ == "__main__":
    print(f"Catalog ready: {len(DESTINATIONS)} destinations")
