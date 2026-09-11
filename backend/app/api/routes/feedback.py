from fastapi import APIRouter, Depends, HTTPException

from ...persistence import Persistence
from ...privacy.session_manager import SessionManager
from ...schemas.recommend import FeedbackRequest
from ..deps import get_persistence, get_session_manager

router = APIRouter()


@router.post("/feedback")
def add_feedback(request: FeedbackRequest, session_manager: SessionManager = Depends(get_session_manager), persistence: Persistence = Depends(get_persistence)) -> dict[str, str]:
    session = session_manager.get(request.session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    session["feedback"].append(request.rating)
    persistence.record({"type": "feedback", "session_id": request.session_id, "rating": request.rating, "destination": request.destination, "action": request.action})
    return {"status": "recorded"}


@router.post("/events/{event_type}")
def record_event(event_type: str, request: FeedbackRequest, session_manager: SessionManager = Depends(get_session_manager), persistence: Persistence = Depends(get_persistence)) -> dict[str, str]:
    if session_manager.get(request.session_id) is None or event_type not in {"click", "save"}:
        raise HTTPException(status_code=404, detail="Session or event not found")
    persistence.record({"type": event_type, "session_id": request.session_id, "destination": request.destination})
    return {"status": "recorded"}
