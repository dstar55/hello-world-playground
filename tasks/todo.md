# Todo

## Task 1: Hello World Python Script ✅
## Task 2: Flask Dashboard Application ✅
## Task 3: Dashboard Section Pages ✅
## Task 4: SQLite Database + OpenAPI Spec ✅

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
- [x] Commit, push, open PR

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
- **database.py**: Added `migrate()` function that uses `PRAGMA table_info` to safely add the `role` column to existing databases. Seed now creates `admin` (role=admin) and `operator` (role=user).
- **app.py**: Login now stores `session["role"]`. Dashboard route passes `current_user` and `current_role` to template. Added `/api/session` (GET), `/api/users` (GET/POST), `/api/users/<id>` (PUT/DELETE) — POST/PUT/DELETE check `session.get("role") != "admin"` and return 403.
- **dashboard.html**: Sidebar bottom now shows avatar icon, username, and role badge (purple for admin, blue for user). Added Users nav item and Users section with table. JS uses `CURRENT_ROLE` variable (embedded from Flask) to show/hide Add/Edit/Delete buttons. Self-delete is disabled. User modal has username, password, and role fields.
- **openapi.yaml**: Added `users` and `session` tags, `/api/session`, `/api/users`, `/api/users/{id}` paths, and `User`, `UserInput`, `SessionInfo` schemas.
