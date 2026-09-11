import importlib

from app.persistence import Persistence


def test_sqlite_backed_persistence_saves_session_and_events(tmp_path):
    persistence = Persistence(f"sqlite:///{tmp_path / 'journeymatch_test.db'}")
    persistence.save_session("session-1", {"budget": 1800, "name": "should be stripped"})
    persistence.record({"type": "recommendation", "session_id": "session-1", "destinations": ["Lisbon"], "preferences": {"interests": ["food"]}})

    with persistence.session_factory() as database:
        stored_session = database.get(persistence.session_model, "session-1")
        assert stored_session is not None
        assert "name" not in stored_session.preferences_json
        assert database.query(persistence.event_model).filter_by(session_id="session-1").count() == 1


def test_sqlite_backed_persistence_deletes_session_and_cascades_events(tmp_path):
    persistence = Persistence(f"sqlite:///{tmp_path / 'journeymatch_test.db'}")
    persistence.save_session("session-2")
    persistence.record({"type": "feedback", "session_id": "session-2", "rating": 5})

    persistence.delete_session("session-2")

    with persistence.session_factory() as database:
        assert database.get(persistence.session_model, "session-2") is None
        assert database.query(persistence.event_model).filter_by(session_id="session-2").count() == 0


def test_memory_only_persistence_is_a_no_op_without_database_url():
    persistence = Persistence(None)
    persistence.save_session("session-3", {"budget": 1000})
    persistence.delete_session("session-3")
    persistence.record({"type": "feedback", "session_id": "session-3", "rating": 4})
    assert persistence.events == [{"type": "feedback", "session_id": "session-3", "rating": 4}]
    assert persistence.session_factory is None
