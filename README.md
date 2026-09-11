# JourneyMatch AI

JourneyMatch is a privacy-first AI travel assistant prototype. Travelers describe a trip in natural language, receive structured preference extraction, compare explainable destination matches, and optionally leave an anonymous satisfaction rating.

## Run locally

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload --port 8000
```

### Frontend

In a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal. Set `VITE_API_URL` when the backend is not on `http://localhost:8000`.

## API

- `GET /health`
- `POST /sessions`
- `DELETE /sessions/{session_id}`
- `POST /recommend`
- `POST /feedback`
- `GET /dashboards/quality`

## Deployment

The root `Dockerfile` builds the React frontend and packages it with FastAPI in one container. The root `railway.json` deploys that single service. Add a Railway PostgreSQL service named `postgres`, then set `DATABASE_URL=${{Postgres.DATABASE_URL}}` on the application service. The backend creates its SQLAlchemy tables on startup and removes session records plus related events on deletion. Frontend API calls use the same origin in the production image.

Verify deployment with:

```powershell
Invoke-RestMethod https://<application-domain>/health
Invoke-RestMethod https://<application-domain>/
```

Expected results are a JSON `status: ok` response from the backend and HTTP 200 HTML from the frontend. Never commit `DATABASE_URL`; use Railway variables.

## Project decisions

The first release uses a deterministic TF-IDF-style keyword baseline rather than a runtime sentence-transformer download. This keeps the cold-start path fast and reproducible while preserving a stable contract for a future embedding or two-tower model. The catalog contains 108 deterministic destination records, and `training/` includes 500 synthetic users, evaluation, and an optional PyTorch two-tower hook. See `docs/` and `notebooks/` for methodology, privacy, limitations, experiments, and architecture.

## Persistence and analytics

When `DATABASE_URL` is set, SQLAlchemy creates `journey_sessions` and `journey_events` tables and records anonymized preferences, recommendation events, ratings, clicks, and saves. Without it, the same API uses process-local memory for development. The quality endpoint exposes satisfaction, click/save rates, response reuse, cold-start coverage, top preference clusters, and most-recommended destinations.
