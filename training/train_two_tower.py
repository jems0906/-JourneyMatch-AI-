"""Optional two-tower training hook.

The baseline product does not require PyTorch. Install the optional `torch` extra
and replace `build_model` with a trained user/destination encoder when data volume
justifies it.
"""


def build_model():
    try:
        import torch
        from torch import nn
    except ImportError as error:
        raise RuntimeError("Install torch to enable the optional two-tower model") from error

    class TwoTower(nn.Module):
        def __init__(self, input_size: int = 16, hidden_size: int = 32):
            super().__init__()
            self.user_tower = nn.Sequential(nn.Linear(input_size, hidden_size), nn.ReLU(), nn.Linear(hidden_size, hidden_size))
            self.destination_tower = nn.Sequential(nn.Linear(input_size, hidden_size), nn.ReLU(), nn.Linear(hidden_size, hidden_size))

        def forward(self, user_features, destination_features):
            return (self.user_tower(user_features) * self.destination_tower(destination_features)).sum(dim=1)

    return TwoTower()


if __name__ == "__main__":
    print("Optional model hook ready; baseline serving remains deterministic.")
