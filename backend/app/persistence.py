import json

from .privacy.data_policy import anonymized_preferences


class Persistence:
    """SQLAlchemy-backed persistence with a privacy-safe memory fallback."""

    def __init__(self, database_url: str | None = None):
        self.events: list[dict] = []
        self.session_factory = None
        if database_url:
            from .models.database import EventRecord, SessionRecord, create_database

            self.session_factory = create_database(database_url)
            self.event_model = EventRecord
            self.session_model = SessionRecord

    def save_session(self, session_id: str, preferences: dict | None = None) -> None:
        if not self.session_factory:
            return
        with self.session_factory() as database:
            database.merge(self.session_model(session_id=session_id, preferences_json=json.dumps(anonymized_preferences(preferences or {}))))
            database.commit()

    def delete_session(self, session_id: str) -> None:
        if not self.session_factory:
            return
        with self.session_factory() as database:
            database.query(self.session_model).filter_by(session_id=session_id).delete()
            database.query(self.event_model).filter_by(session_id=session_id).delete()
            database.commit()

    def record(self, event: dict) -> None:
        self.events.append(event)
        if not self.session_factory:
            return
        with self.session_factory() as database:
            database.add(self.event_model(session_id=event["session_id"], event_type=event["type"], destination=event.get("destination"), payload_json=json.dumps(event)))
            database.commit()
