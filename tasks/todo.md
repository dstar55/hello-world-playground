# Todo

## Task 1: Hello World Python Script ✅

## Task 2: Flask Dashboard Application

### Plan
- [x] git pull main
- [x] Create GitHub issue
- [x] Create branch `feature/issue-3-dashboard-app`
- [x] Create `requirements.txt` (Flask only)
- [x] Create `app.py` with routes: `/`, `/login`, `/dashboard`, `/logout`
- [x] Create `templates/base.html`
- [x] Create `templates/login.html`
- [x] Create `templates/dashboard.html`
- [x] Commit with co-author note
- [x] Push branch and open PR linked to the issue

### Notes
- Login: admin/admin, session-based, no database
- Sidebar nav items: Email Processor, Fleet Management, Branches, Bookings, Calendar, Analytics, Konkurencija
- Dashboard cards: Total Vehicles (160), Available (123), Branches (14), Vehicle Classes (14)
- Dark sidebar (#1a1f2e), light main content area
- Bootstrap 5 via CDN

## Review
- Created `app.py` with Flask routes and session-based auth (admin/admin)
- Created `requirements.txt` with Flask dependency
- Created 3 templates: base.html, login.html, dashboard.html
- Dashboard has dark sidebar with nav items and 4 stats cards matching the design
- GitHub issue #3 created, PR linked with `Fixes #3`
