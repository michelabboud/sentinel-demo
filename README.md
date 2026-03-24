# Sentinel Demo

A task management web app built with **FastAPI + Vue 3** — designed as a test target for [Sentinel](https://github.com/michelabboud/sentinel-sweep) QA sweeps.

This project contains **10 intentional bugs** that Sentinel should detect across RBAC, security, a11y, i18n, performance, and CSS categories.

## Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Vue 3, Vite, Vue Router, vue-i18n, Tailwind CSS v4 |
| Backend | FastAPI, SQLAlchemy, SQLite, JWT auth (python-jose) |
| Auth | JWT with 3 roles: admin, manager, user |

## Quick Start

```bash
# Backend
cd backend
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
python seed.py
uvicorn app.main:app --port 8000

# Frontend (separate terminal)
cd frontend
npm install
npm run dev
```

- Frontend: http://localhost:5173
- API: http://localhost:8000
- API docs: http://localhost:8000/docs

## Test Credentials

| Role | Email | Password |
|------|-------|----------|
| admin | admin@demo.com | Admin123! |
| manager | manager@demo.com | Manager123! |
| user | user@demo.com | User123! |

## Running Sentinel Against This Project

```bash
# Install Sentinel plugin (if not already installed)
claude plugin install sentinel@sentinel-marketplace

# From this project directory:
/sentinel:run setup              # Verify environment
/sentinel:run api --safe-only    # Quick API health check
/sentinel:run sweep              # Full browser + API sweep
/sentinel:run report --dashboard # View health score
```

## Intentional Bugs

These bugs are planted for Sentinel to detect. Do not fix them — they are the test cases.

| # | Category | Severity | Description | File |
|---|----------|----------|-------------|------|
| 1 | RBAC | Critical | `/api/v1/groups/{id}/members` has no auth — accessible without login | `backend/app/endpoints/groups.py` |
| 2 | RBAC | Critical | `/api/v1/tasks/debug/info` has no auth — leaks internal data | `backend/app/endpoints/tasks.py` |
| 3 | Security | Error | Debug endpoint leaks stack traces and database URL | `backend/app/endpoints/tasks.py` |
| 4 | Performance | Warning | N+1 query in `list_group_members` — queries tasks per member in a loop | `backend/app/endpoints/groups.py` |
| 5 | i18n | Warning | 18 French translation keys missing (53% coverage vs 100% English) | `frontend/src/locales/fr.json` |
| 6 | a11y | Error | Login form inputs have no `<label>` elements | `frontend/src/views/LoginView.vue` |
| 7 | a11y | Error | Dashboard banner `<img>` has no `alt` attribute | `frontend/src/views/DashboardView.vue` |
| 8 | a11y | Error | Logout button has only an icon, no `aria-label` | `frontend/src/App.vue` |
| 9 | a11y | Warning | Task delete uses `<div @click>` without keyboard handler | `frontend/src/views/TasksView.vue` |
| 10 | CSS | Info | Unused classes `.legacy-banner` and `.old-card-style` | `frontend/src/assets/app.css` |

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/api/v1/auth/login` | None | Login, returns JWT |
| GET | `/api/v1/users/` | Admin | List all users |
| POST | `/api/v1/users/` | Admin | Create user |
| GET | `/api/v1/users/{id}` | User | Get user by ID |
| PATCH | `/api/v1/users/{id}` | Admin | Update user |
| DELETE | `/api/v1/users/{id}` | Admin | Delete user (cascade) |
| GET | `/api/v1/groups/` | User | List all groups |
| POST | `/api/v1/groups/` | Manager | Create group |
| GET | `/api/v1/groups/{id}` | User | Get group by ID |
| PATCH | `/api/v1/groups/{id}` | Manager | Update group |
| DELETE | `/api/v1/groups/{id}` | Manager | Delete group (cascade) |
| GET | `/api/v1/groups/{id}/members` | **None (bug)** | List group members |
| GET | `/api/v1/tasks/` | User | List all tasks |
| POST | `/api/v1/tasks/` | User | Create task |
| GET | `/api/v1/tasks/{id}` | User | Get task by ID |
| PATCH | `/api/v1/tasks/{id}` | User | Update task |
| DELETE | `/api/v1/tasks/{id}` | Manager | Delete task |
| GET | `/api/v1/tasks/debug/info` | **None (bug)** | Debug info (leaks data) |

## Frontend Routes

| Path | View | Required Role |
|------|------|---------------|
| `/login` | LoginView | None |
| `/dashboard` | DashboardView | User |
| `/tasks` | TasksView | User |
| `/tasks/:id` | TaskDetailView | User |
| `/groups` | GroupsView | User |
| `/groups/:id` | GroupDetailView | User |
| `/admin/users` | UsersView | Admin |
| `/admin/settings` | SettingsView | Admin |

## License

MIT
