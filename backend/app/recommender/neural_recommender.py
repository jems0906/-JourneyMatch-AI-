from typing import Any


def load_two_tower_model(path: str | None = None) -> Any:
    """Load an optional PyTorch checkpoint when one is configured."""
    if not path:
        return None
    try:
        import torch
    except ImportError as error:
        raise RuntimeError("Install torch to load the optional two-tower model") from error
    return torch.load(path, map_location="cpu", weights_only=False)


def neural_score(model: Any, user_features: Any, destination_features: Any) -> float:
    if model is None:
        return 0.0
    return float(model(user_features, destination_features).item())
