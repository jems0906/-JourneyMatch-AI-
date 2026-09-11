from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .api import router
from .config import settings
from .middleware import RateLimitMiddleware
from .persistence import Persistence
from .privacy.session_manager import SessionManager

app = FastAPI(title=settings.app_name, version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins.split(","), allow_methods=["*"], allow_headers=["*"])
app.add_middleware(RateLimitMiddleware, requests_per_minute=settings.rate_limit_per_minute)
app.state.session_manager = SessionManager()
app.state.persistence = Persistence(settings.database_url)
app.include_router(router)

frontend_dist = Path(__file__).parents[2] / "frontend" / "dist"
if frontend_dist.exists():
	app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")

# kept for backward-compatible test/notebook access to in-memory state
sessions = app.state.session_manager.sessions
events = app.state.persistence.events
