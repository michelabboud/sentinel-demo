# CLAUDE.md

## Project Overview

**Sentinel Demo** — A task management web application for testing Sentinel QA sweeps.

- **Frontend**: Vue 3 + Vite + Vue Router + vue-i18n + Tailwind CSS v4
- **Backend**: FastAPI + SQLAlchemy + SQLite + JWT auth
- **Architecture**: SPA frontend with REST API backend

## Ports

| Service  | Port |
|----------|------|
| Frontend | 5173 |
| API      | 8000 |

## API Base URL

`http://localhost:8000`

## Frontend Base URL

`http://localhost:5173`

## Test Credentials

| Role    | Email              | Password     |
|---------|--------------------|-------------|
| admin   | admin@demo.com     | Admin123!   |
| manager | manager@demo.com   | Manager123! |
| user    | user@demo.com      | User123!    |

## Starting the Application

### Backend
```bash
cd backend
pip install -r requirements.txt
python seed.py          # Seed the database
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Database

SQLite at `backend/sentinel_demo.db`. Re-seed with `python seed.py`.

## Known Intentional Bugs (for Sentinel testing)

1. `/api/v1/groups/{id}/members` has NO auth — any unauthenticated user can access it
2. `/api/v1/tasks/debug/info` leaks stack traces and database URL
3. N+1 query in `list_group_members` — queries tasks individually per member
4. Missing i18n keys in French locale (nav.settings, nav.logout, dashboard.recentActivity, errors.*)
5. Missing form labels on login page (a11y)
6. Image without alt attribute on dashboard (a11y)
7. Button with only icon, no aria-label in navbar (a11y)
8. Click handler on div without keyboard support in tasks table (a11y)
9. Unused CSS classes: `.legacy-banner`, `.old-card-style`
10. Task POST endpoint accepts empty body without validation
