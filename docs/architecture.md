# Architecture

The backend is a FastAPI service with four focused responsibilities: session lifecycle, preference extraction, recommendation scoring, and aggregate quality metrics. The frontend is a static React/Vite app that talks to the backend over JSON HTTP. Railway can run each Dockerfile as an independent service.

The current process-local session store intentionally keeps the deployment demonstrable without a database. PostgreSQL can be introduced behind the same service functions when persistence and multi-instance analytics are required.
