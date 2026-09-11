"""Run the full local training/data pipeline in sequence."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
STEPS = [
    [sys.executable, str(ROOT / "scripts" / "build_destination_dataset.py")],
    [sys.executable, str(ROOT / "training" / "generate_synthetic_users.py")],
    [sys.executable, str(ROOT / "training" / "evaluate.py")],
]

if __name__ == "__main__":
    for step in STEPS:
        print(f"$ {' '.join(step)}")
        subprocess.run(step, check=True, cwd=ROOT)
