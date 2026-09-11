# Model Card

## Intended use

Directional travel inspiration for a cold-start customer experience prototype.

## Training and data

The current baseline does not train on personal data. Destination attributes are curated sample data in `data_samples/destinations.csv`. Feedback is held in process memory for demonstration analytics.

## Limitations

The keyword extractor is English-only, airport distance is approximated, costs are illustrative, and accessibility flags require verification with operators before booking. Scores are not guarantees of availability, safety, or suitability.

## Human factors

Recommendations should be reviewed by the traveler. The interface labels match dimensions so users can understand why an item was selected rather than treating the score as an authority.
