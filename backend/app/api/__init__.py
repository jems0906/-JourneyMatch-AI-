"""HTTP API boundary."""

from fastapi import APIRouter

from .routes import dashboards, feedback, health, recommend, sessions

router = APIRouter()
router.include_router(health.router)
router.include_router(sessions.router)
router.include_router(recommend.router)
router.include_router(feedback.router)
router.include_router(dashboards.router)
