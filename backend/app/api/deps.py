from fastapi import Request

from ..persistence import Persistence
from ..privacy.session_manager import SessionManager


def get_session_manager(request: Request) -> SessionManager:
    return request.app.state.session_manager


def get_persistence(request: Request) -> Persistence:
    return request.app.state.persistence
