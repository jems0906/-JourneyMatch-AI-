from uuid import uuid4


class SessionManager:
    def __init__(self):
        self.sessions: dict[str, dict] = {}

    def create(self) -> str:
        session_id = str(uuid4())
        self.sessions[session_id] = {"recommendations": 0, "feedback": []}
        return session_id

    def delete(self, session_id: str) -> None:
        self.sessions.pop(session_id, None)

    def get(self, session_id: str) -> dict | None:
        return self.sessions.get(session_id)
