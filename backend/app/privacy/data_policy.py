FORBIDDEN_PERSISTED_FIELDS = {"name", "email", "payment", "loyalty_number", "raw_profile"}


def anonymized_preferences(preferences: dict) -> dict:
    return {key: value for key, value in preferences.items() if key not in FORBIDDEN_PERSISTED_FIELDS}
