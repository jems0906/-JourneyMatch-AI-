# Trained Models

This project ships a deterministic scoring baseline that requires no trained
artifacts. `two_tower_model.pt` is not committed because the optional
two-tower model in `training/train_two_tower.py` is a hook for future work,
not part of the default serving path. Run that script after installing
`torch` to produce a local checkpoint here.
