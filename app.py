from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

DASHBOARD_STATS = [
    {"title": "TOTAL VEHICLES", "value": "160", "subtitle": "Active fleet", "icon": "bi-car-front"},
    {"title": "AVAILABLE", "value": "123", "subtitle": "Ready to rent", "icon": "bi-check-circle"},
    {"title": "BRANCHES", "value": "14", "subtitle": "Locations", "icon": "bi-building"},
    {"title": "VEHICLE CLASSES", "value": "14", "subtitle": "Categories", "icon": "bi-stars"},
]

NAV_ITEMS = [
    {"name": "Email Processor", "icon": "bi-envelope"},
    {"name": "Fleet Management", "icon": "bi-car-front"},
    {"name": "Branches", "icon": "bi-geo-alt"},
    {"name": "Bookings", "icon": "bi-file-text"},
    {"name": "Calendar", "icon": "bi-calendar"},
    {"name": "Analytics", "icon": "bi-bar-chart"},
    {"name": "Konkurencija", "icon": "bi-graph-up"},
]


@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))
        error = "Invalid credentials. Please try again."
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", stats=DASHBOARD_STATS, nav_items=NAV_ITEMS)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
