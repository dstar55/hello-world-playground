# Todo

## Task 1: Hello World Python Script ✅
## Task 2: Flask Dashboard Application ✅

## Task 3: Dashboard Section Pages

### Plan
- [x] git pull main
- [x] Create GitHub issue #5
- [x] Create branch `feature/issue-5-dashboard-sections`
- [x] Update `tasks/todo.md`
- [ ] Update `base.html` — add Chart.js + Leaflet.js CDN
- [ ] Update `dashboard.html` — all 8 sections with JS navigation
- [ ] Commit, push, open PR

### Sections
| Section         | UI Pattern |
|----------------|-----------|
| Dashboard       | Existing stats cards (keep) |
| Email Processor | Table, status badges, add/delete/mark-read |
| Fleet Management| Clickable cards grid, detail modal |
| Branches        | Leaflet map + editable list (add/edit/delete) |
| Bookings        | Table with add/edit/delete modal form |
| Calendar        | Monthly grid calendar with events |
| Analytics       | Chart.js: line, bar, doughnut charts |
| Konkurencija    | Competitor comparison cards |

### Notes
- Single dashboard.html, JS show/hide sections
- All data hardcoded in JS arrays
- Refresh button top-right on every section
- Chart.js + Leaflet.js via CDN
