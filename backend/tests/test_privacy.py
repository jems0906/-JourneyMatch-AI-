from app.privacy.data_policy import FORBIDDEN_PERSISTED_FIELDS, anonymized_preferences
from app.privacy.session_manager import SessionManager


def test_anonymized_preferences_strips_forbidden_fields():
    raw = {"budget": 1500, "name": "Jane Doe", "email": "jane@example.com", "payment": "4111", "loyalty_number": "SKY123", "raw_profile": {"anything": True}}
    cleaned = anonymized_preferences(raw)
    assert cleaned == {"budget": 1500}
    assert not FORBIDDEN_PERSISTED_FIELDS.intersection(cleaned)


def test_anonymized_preferences_keeps_travel_fields():
    preferences = {"budget": 2000, "climate": "warm", "interests": ["food", "beach"], "accessibility": True}
    assert anonymized_preferences(preferences) == preferences


def test_session_manager_create_get_delete_lifecycle():
    manager = SessionManager()
    session_id = manager.create()
    assert manager.get(session_id) == {"recommendations": 0, "feedback": []}
    manager.delete(session_id)
    assert manager.get(session_id) is None


def test_session_manager_delete_unknown_session_is_a_no_op():
    manager = SessionManager()
    manager.delete("does-not-exist")
