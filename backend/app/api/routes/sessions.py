from fastapi import APIRouter, Depends

from ...persistence import Persistence
from ...privacy.session_manager import SessionManager
from ...schemas.session import SessionResponse
from ..deps import get_persistence, get_session_manager

router = APIRouter()


@router.post("/sessions", response_model=SessionResponse)
def create_session(session_manager: SessionManager = Depends(get_session_manager), persistence: Persistence = Depends(get_persistence)) -> SessionResponse:
    session_id = session_manager.create()
    persistence.save_session(session_id)
    return SessionResponse(session_id=session_id)


@router.delete("/sessions/{session_id}", status_code=204)
def delete_session(session_id: str, session_manager: SessionManager = Depends(get_session_manager), persistence: Persistence = Depends(get_persistence)) -> None:
    session_manager.delete(session_id)
    persistence.delete_session(session_id)
