# Todo

## Task 1: Hello World Python Script ✅

### Plan
- [x] git pull main
- [x] Create GitHub issue #1
- [x] Create branch `feature/issue-1-hello-world`
- [x] Create `hello_world.py`
- [x] Commit, push, open PR #2

### Changes per file
| File | Change |
|------|--------|
| `hello_world.py` | Created with `main()` function that prints "Hello, World!" |

### Review
- **hello_world.py**: Simple script with `main()` entry point pattern and `if __name__ == "__main__": main()` guard, ready for future extension.

---

## Task 2: Flask Dashboard Application ✅

### Plan
- [x] git pull main
- [x] Create GitHub issue #3
- [x] Create branch `feature/issue-3-dashboard-app`
- [x] Create `requirements.txt` (Flask)
- [x] Create `app.py` — Flask app with login route and dashboard route
- [x] Create `templates/base.html` — Bootstrap 5 base layout
- [x] Create `templates/login.html` — login card with admin/admin credentials
- [x] Create `templates/dashboard.html` — sidebar + stat cards
- [x] Commit, push, open PR #4

### Changes per file
| File | Change |
|------|--------|
| `requirements.txt` | Added `Flask==3.0.0` |
| `app.py` | Flask app with session-based login (admin/admin), dashboard and logout routes |
| `templates/base.html` | Bootstrap 5.3 + Bootstrap Icons 1.11 via CDN |
| `templates/login.html` | Centered card with RentACar branding and login form |
| `templates/dashboard.html` | Dark sidebar (#1a1f2e), 4 stat cards, hardcoded JS nav |

### Review
- **app.py**: Session-based auth (`session["user"]`). Login checks hardcoded admin/admin, redirects to dashboard. Logout clears session.
- **dashboard.html**: Dark sidebar with Bootstrap nav-pills. Stats rendered via Jinja2 loop from `DASHBOARD_STATS` list. Single-page JS show/hide section navigation pattern established.

---

## Task 3: Dashboard Section Pages ✅

### Plan
- [x] git pull main
- [x] Create GitHub issue #5
- [x] Create branch `feature/issue-5-dashboard-sections`
- [x] Update `templates/base.html` — add Chart.js 4.4 + Leaflet.js 1.9 CDN
- [x] Update `templates/dashboard.html` — all 8 sections with JS navigation + hardcoded data
- [x] Commit, push, open PR #6

### Sections
| Section | UI Pattern |
|---------|-----------|
| Dashboard | Stat cards (keep existing) |
| Email Processor | Table with status badges, mark-read and delete actions |
| Fleet Management | Clickable card grid, vehicle detail modal |
| Branches | Leaflet interactive map + editable table (add/edit/delete) |
| Bookings | Table with add/edit/delete modal form |
| Calendar | Monthly grid calendar with event badges |
| Analytics | Chart.js: line (revenue), doughnut (fleet status), bar (bookings) |
| Konkurencija | Competitor comparison cards with market share progress bar |

### Changes per file
| File | Change |
|------|--------|
| `templates/base.html` | Added Chart.js 4.4 and Leaflet.js 1.9 via CDN |
| `templates/dashboard.html` | 8 content sections, JS show/hide navigation, all data hardcoded in JS arrays |

### Review
- Single `dashboard.html` file with all 8 sections; JS `showSection()` hides all then shows target.
- All data was hardcoded in JS arrays at this stage (replaced with API calls in Task 4).
- Chart.js used for analytics (line, doughnut, bar). Leaflet.js used for branch map.
- Refresh button on every section for UX consistency.

---

## Task 4: SQLite Database + OpenAPI Spec ✅

### Plan
- [x] git pull main
- [x] Create GitHub issue #7
- [x] Create branch `feature/issue-7-sqlite-database`
- [x] Update `requirements.txt` — add Flask-SQLAlchemy
- [x] Create `models.py` — 7 SQLAlchemy models
- [x] Create `database.py` — seed function
- [x] Update `app.py` — init DB, CRUD API endpoints, login queries DB
- [x] Update `templates/dashboard.html` — replace JS arrays with fetch() API calls
- [x] Create `openapi.yaml` — OpenAPI 3.0 specification
- [x] Commit, push, open PR #8

### Models
| Model | Fields |
|-------|--------|
| User | id, username, password |
| Email | id, from_email, subject, date, status |
| Vehicle | id, make, model, plate, status, cls, year, mileage |
| Branch | id, name, city, address, phone, lat, lng |
| Booking | id, booking_ref, customer, vehicle, from_date, to_date, status |
| CalendarEvent | id, date, title, color |
| Competitor | id, name, rating, daily_price, market_share, vehicles, trend |

### Changes per file
| File | Change |
|------|--------|
| `requirements.txt` | Added `Flask-SQLAlchemy==3.1.1` |
| `models.py` | 7 SQLAlchemy models, each with `to_dict()` serializer |
| `database.py` | `seed_data()` with guard (`if User.query.first(): return`) and sample data |
| `app.py` | `db.init_app()`, login queries DB, CRUD endpoints for emails/branches/bookings, GET for vehicles/events/competitors |
| `templates/dashboard.html` | Replaced all hardcoded JS arrays with `fetch()` calls via `api()` helper; added cache arrays (vehiclesCache, branchesCache, bookingsCache) |
| `openapi.yaml` | OpenAPI 3.0 spec: all endpoints, request/response schemas |

### Review
- **models.py**: All 7 models with `to_dict()` for clean JSON serialization. No relationships (kept simple with string references).
- **database.py**: Single `seed_data()` called at app startup. Guard prevents re-seeding on restart.
- **app.py**: RESTful endpoints following `/api/<resource>` pattern. Login now authenticates against DB instead of hardcoded string.
- **dashboard.html**: `api()` helper wraps fetch with JSON headers. All CRUD sections (email, branches, bookings) use full create/update/delete cycle. Fleet, events, competitors are GET-only.
- **openapi.yaml**: Full spec covering all endpoints with schemas, request bodies, and response codes.

---

## Task 5: User Management with Roles ✅

### Plan
- [x] git pull main
- [x] Create GitHub issue #9
- [x] Create branch `feature/issue-9-user-management`
- [x] Update `models.py` — add `role` field to User model
- [x] Update `database.py` — seed admin (role=admin) + add operator user (role=user) + migration
- [x] Update `app.py` — user CRUD API endpoints + `/api/session` + role in session
- [x] Update `dashboard.html` — Users section + sidebar username/role display
- [x] Update `openapi.yaml` — add user management + session endpoints
- [x] Commit, push, open PR #10

### Role Design
| Role  | Permissions |
|-------|------------|
| admin | Full access: view/add/edit/delete all users |
| user  | Restricted: view users list only, cannot add/edit/delete |

### Changes per file
| File | Change |
|------|--------|
| `models.py` | Added `role` field (admin/user) to User model + `to_dict()` |
| `database.py` | Added `migrate()` for existing DBs + seeded operator user (role=user) |
| `app.py` | Store role in session on login, pass to template, added `/api/session` + user CRUD (admin-guarded) |
| `dashboard.html` | New Users nav item + Users section + sidebar shows username + role badge |
| `openapi.yaml` | Added user management endpoints + session endpoint + User/UserInput/SessionInfo schemas |

### Review
- **models.py**: Added `role = db.Column(db.String(20), nullable=False, default='user')` and `to_dict()` to User model.
- **database.py**: Added `migrate()` function that uses `PRAGMA table_info` to safely add the `role` column to existing databases. Also always ensures `admin` user has `role='admin'` (fixes DEFAULT 'user' migration bug). Seed now creates `admin` (role=admin) and `operator` (role=user).
- **app.py**: Login now stores `session["role"]`. Dashboard route passes `current_user` and `current_role` to template. Added `/api/session` (GET), `/api/users` (GET/POST), `/api/users/<id>` (PUT/DELETE) — POST/PUT/DELETE check `session.get("role") != "admin"` and return 403.
- **dashboard.html**: Sidebar nav wrapped in scrollable div (fixes two-column layout bug). Sidebar bottom shows avatar icon, username, and role badge (purple for admin, blue for user). Added Users nav item and Users section with table. JS uses `CURRENT_ROLE` variable (embedded from Flask) to show/hide Add/Edit/Delete buttons. Self-delete is disabled.
- **openapi.yaml**: Added `users` and `session` tags, `/api/session`, `/api/users`, `/api/users/{id}` paths, and `User`, `UserInput`, `SessionInfo` schemas.

---

## Task 6: Move User Info and Logout to Top-Right Corner

### Plan
- [x] git pull main
- [x] Create GitHub issue #11
- [x] Create branch `feature/issue-11-topbar-user-logout`
- [x] Update `templates/dashboard.html`:
  - Remove user info + logout from sidebar bottom
  - Add topbar to main content area with user avatar, username, role badge and logout button on the right
- [x] Commit, push, open PR

### Design
- Remove the bottom `div` (user info + logout) from the sidebar entirely
- Add a thin topbar at the top of the main content column: white background, border-bottom, user info on the right with a Logout button
- Sidebar becomes nav-only (logo + nav items), cleaner and without scroll concern
- Topbar sticks to the top of the content area, always visible

### Changes per file
| File | Change |
|------|--------|
| `templates/dashboard.html` | Removed user info + logout from sidebar bottom; added topbar (56px, white, border-bottom) with avatar, username, role badge and Logout button on the right |

### Review
- **dashboard.html**: Sidebar bottom block removed entirely — sidebar is now nav-only. Main content column changed to `d-flex flex-column` with a `flex-shrink-0` topbar (fixed 56px height, white background, border-bottom). User avatar, username, role badge (purple for admin, blue for user) and Logout button sit on the right side of the topbar, always visible regardless of scroll or screen size.

---

## Task 7: Light/Dark Theme Switcher

### Plan
- [x] git pull main
- [x] Create GitHub issue #13
- [x] Create branch `feature/issue-13-theme-switcher`
- [x] Update `templates/base.html` — add inline script to apply saved theme before render (prevents flash)
- [x] Update `templates/dashboard.html` — add sun/moon toggle button to topbar
- [x] Commit, push, open PR

### Design
- Use Bootstrap 5.3 native dark mode (`data-bs-theme` attribute on `<html>`)
- Default: `light`
- Toggle: sun icon (☀) in dark mode → click → switches to light; moon icon (☾) in light mode → click → switches to dark
- Preference saved in `localStorage` key `theme`
- Inline `<script>` in `<head>` of `base.html` reads `localStorage` and sets `data-bs-theme` before page paint — prevents white flash on dark mode reload
- Topbar toggle button placed left of the user avatar in the topbar

### Changes per file
| File | Change |
|------|--------|
| `templates/base.html` | Added `data-bs-theme="light"` to `<html>` tag; inline script in `<head>` to read `localStorage` and apply theme before render; removed hardcoded `body { background-color }` |
| `templates/dashboard.html` | Changed topbar `bg-white` → `bg-body` (theme-aware); added moon/sun toggle button; `toggleTheme()` JS function + page-load icon sync IIFE |

### Review
- **base.html**: Inline script runs before CSS loads — sets `data-bs-theme` from `localStorage` — prevents flash of wrong theme on page reload. Default `data-bs-theme="light"` on `<html>` is the fallback when no preference is saved. Hardcoded body background removed so Bootstrap dark mode can control it.
- **dashboard.html**: Topbar button shows moon icon in light mode, sun icon in dark mode. `toggleTheme()` reads current theme, toggles it, saves to `localStorage`, updates icon. An IIFE on page load syncs the icon to match the current theme (handles the case where the page loads already in dark mode from `localStorage`).
