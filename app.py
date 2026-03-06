from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from models import db, User, Email, Vehicle, Branch, Booking, CalendarEvent, Competitor
from database import seed_data

app = Flask(__name__)
app.secret_key = "dev-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rentacar.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    seed_data()

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


# --- Auth routes ---

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
        user = User.query.filter_by(username=username, password=password).first()
        if user:
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


# --- API: Emails ---

@app.route("/api/emails", methods=["GET"])
def get_emails():
    return jsonify([e.to_dict() for e in Email.query.order_by(Email.date.desc()).all()])


@app.route("/api/emails", methods=["POST"])
def create_email():
    data = request.json
    email = Email(from_email=data["from"], subject=data["subject"],
                  date=data["date"], status=data.get("status", "New"))
    db.session.add(email)
    db.session.commit()
    return jsonify(email.to_dict()), 201


@app.route("/api/emails/<int:id>", methods=["PUT"])
def update_email(id):
    email = db.get_or_404(Email, id)
    data = request.json
    if "status" in data:
        email.status = data["status"]
    db.session.commit()
    return jsonify(email.to_dict())


@app.route("/api/emails/<int:id>", methods=["DELETE"])
def delete_email(id):
    email = db.get_or_404(Email, id)
    db.session.delete(email)
    db.session.commit()
    return "", 204


# --- API: Vehicles ---

@app.route("/api/vehicles", methods=["GET"])
def get_vehicles():
    return jsonify([v.to_dict() for v in Vehicle.query.all()])


# --- API: Branches ---

@app.route("/api/branches", methods=["GET"])
def get_branches():
    return jsonify([b.to_dict() for b in Branch.query.all()])


@app.route("/api/branches", methods=["POST"])
def create_branch():
    data = request.json
    branch = Branch(name=data["name"], city=data["city"], address=data["address"],
                    phone=data["phone"], lat=data.get("lat", 45.0), lng=data.get("lng", 16.0))
    db.session.add(branch)
    db.session.commit()
    return jsonify(branch.to_dict()), 201


@app.route("/api/branches/<int:id>", methods=["PUT"])
def update_branch(id):
    branch = db.get_or_404(Branch, id)
    data = request.json
    for field in ["name", "city", "address", "phone"]:
        if field in data:
            setattr(branch, field, data[field])
    db.session.commit()
    return jsonify(branch.to_dict())


@app.route("/api/branches/<int:id>", methods=["DELETE"])
def delete_branch(id):
    branch = db.get_or_404(Branch, id)
    db.session.delete(branch)
    db.session.commit()
    return "", 204


# --- API: Bookings ---

@app.route("/api/bookings", methods=["GET"])
def get_bookings():
    return jsonify([b.to_dict() for b in Booking.query.all()])


@app.route("/api/bookings", methods=["POST"])
def create_booking():
    data = request.json
    count = Booking.query.count() + 1
    booking = Booking(
        booking_ref=data.get("booking_ref", f"BK-{count:03d}"),
        customer=data["customer"], vehicle=data["vehicle"],
        from_date=data["from_date"], to_date=data["to_date"],
        status=data.get("status", "Pending")
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify(booking.to_dict()), 201


@app.route("/api/bookings/<int:id>", methods=["PUT"])
def update_booking(id):
    booking = db.get_or_404(Booking, id)
    data = request.json
    for field in ["customer", "vehicle", "from_date", "to_date", "status"]:
        if field in data:
            setattr(booking, field, data[field])
    db.session.commit()
    return jsonify(booking.to_dict())


@app.route("/api/bookings/<int:id>", methods=["DELETE"])
def delete_booking(id):
    booking = db.get_or_404(Booking, id)
    db.session.delete(booking)
    db.session.commit()
    return "", 204


# --- API: Calendar Events ---

@app.route("/api/events", methods=["GET"])
def get_events():
    return jsonify([e.to_dict() for e in CalendarEvent.query.order_by(CalendarEvent.date).all()])


# --- API: Competitors ---

@app.route("/api/competitors", methods=["GET"])
def get_competitors():
    return jsonify([c.to_dict() for c in Competitor.query.all()])


if __name__ == "__main__":
    app.run(debug=True)
