from fastapi import APIRouter, Depends, HTTPException

from ...nlp import extract_preferences
from ...persistence import Persistence
from ...privacy.session_manager import SessionManager
from ...recommender import recommend as run_recommend
from ...schemas.recommend import RecommendationRequest
from ..deps import get_persistence, get_session_manager

router = APIRouter()


@router.post("/recommend")
def get_recommendations(request: RecommendationRequest, session_manager: SessionManager = Depends(get_session_manager), persistence: Persistence = Depends(get_persistence)) -> dict:
    session = session_manager.get(request.session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    preferences = extract_preferences(request.prompt)
    results = run_recommend(preferences)
    reused = session["recommendations"] > len(results)
    session.update({"preferences": preferences, "recommendations": session["recommendations"] + len(results)})
    persistence.record({"type": "recommendation", "session_id": request.session_id, "preferences": preferences, "destinations": [item["city"] for item in results], "reused": reused})
    persistence.save_session(request.session_id, preferences)
    return {"preferences": preferences, "recommendations": results}
