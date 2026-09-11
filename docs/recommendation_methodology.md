# Recommendation Methodology

JourneyMatch uses a transparent hybrid baseline designed for cold-start behavior.

1. Preference extraction detects budget, climate, airport codes, accessibility language, duration, and interests from user-supplied text.
2. Content matching compares extracted interests and climate to curated destination attributes.
3. Weighted scoring combines budget fit (28%), interest fit (28%), climate fit (22%), accessibility (14%), and flight-origin fit (8%).
4. Explanations are generated from the dimensions that score at least 70%.

The baseline is intentionally deterministic and does not require downloading a model at runtime. A future sentence-transformer or two-tower model can be added behind the same recommendation contract and evaluated against this baseline.
