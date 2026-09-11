from fastapi import APIRouter, Depends

from ...analytics.quality_metrics import summarize
from ...persistence import Persistence
from ...privacy.session_manager import SessionManager
from ..deps import get_persistence, get_session_manager

router = APIRouter()


@router.get("/dashboards/quality")
def quality_dashboard(session_manager: SessionManager = Depends(get_session_manager), persistence: Persistence = Depends(get_persistence)) -> dict:
    return summarize(persistence.events, session_manager.sessions)
