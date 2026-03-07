from sqlalchemy import text
from models import db, User, Email, Vehicle, Branch, Booking, CalendarEvent, Competitor


def migrate():
    """Add role column to user table if it doesn't exist."""
    with db.engine.connect() as conn:
        columns = [row[1] for row in conn.execute(text("PRAGMA table_info(user)"))]
        if "role" not in columns:
            conn.execute(text("ALTER TABLE user ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT 'user'"))
            conn.commit()


def seed_data():
    migrate()

    if User.query.first():
        return  # Already seeded

    db.session.add(User(username="admin", password="admin", role="admin"))
    db.session.add(User(username="operator", password="operator", role="user"))

    for e in [
        Email(from_email="john.doe@email.com", subject="Booking Request #1234", date="2026-03-05", status="New"),
        Email(from_email="jane.smith@email.com", subject="Vehicle Return Confirmation", date="2026-03-04", status="Read"),
        Email(from_email="mike.jones@email.com", subject="Invoice #5678", date="2026-03-03", status="Replied"),
        Email(from_email="sarah.wilson@email.com", subject="Damage Report - Toyota Camry", date="2026-03-02", status="New"),
        Email(from_email="support@insurance.com", subject="Policy Renewal Notice", date="2026-03-01", status="Read"),
    ]:
        db.session.add(e)

    for v in [
        Vehicle(make="Toyota", model="Camry", plate="ZG-123-AB", status="Available", cls="Economy", year=2022, mileage="45,200 km"),
        Vehicle(make="BMW", model="Series 3", plate="ZG-456-CD", status="Rented", cls="Premium", year=2023, mileage="12,800 km"),
        Vehicle(make="Volkswagen", model="Golf", plate="ZG-789-EF", status="Available", cls="Economy", year=2021, mileage="67,400 km"),
        Vehicle(make="Mercedes", model="C-Class", plate="ZG-321-GH", status="Maintenance", cls="Luxury", year=2023, mileage="8,900 km"),
        Vehicle(make="Audi", model="A4", plate="ZG-654-IJ", status="Available", cls="Premium", year=2022, mileage="31,100 km"),
        Vehicle(make="Ford", model="Focus", plate="ZG-987-KL", status="Rented", cls="Economy", year=2021, mileage="54,700 km"),
        Vehicle(make="Hyundai", model="Tucson", plate="ZG-147-MN", status="Available", cls="SUV", year=2023, mileage="19,300 km"),
        Vehicle(make="Kia", model="Sportage", plate="ZG-258-OP", status="Available", cls="SUV", year=2022, mileage="28,600 km"),
    ]:
        db.session.add(v)

    for b in [
        Branch(name="Zagreb Center", city="Zagreb", address="Ilica 123", phone="+385 1 234 5678", lat=45.8150, lng=15.9819),
        Branch(name="Zagreb Airport", city="Zagreb", address="Pleso bb", phone="+385 1 234 5679", lat=45.7429, lng=16.0688),
        Branch(name="Split Center", city="Split", address="Marmontova 45", phone="+385 21 234 567", lat=43.5081, lng=16.4402),
        Branch(name="Dubrovnik", city="Dubrovnik", address="Stradun 12", phone="+385 20 234 567", lat=42.6507, lng=18.0944),
        Branch(name="Rijeka", city="Rijeka", address="Korzo 67", phone="+385 51 234 567", lat=45.3271, lng=14.4422),
    ]:
        db.session.add(b)

    for bk in [
        Booking(booking_ref="BK-001", customer="John Doe", vehicle="Toyota Camry", from_date="2026-03-01", to_date="2026-03-05", status="Completed"),
        Booking(booking_ref="BK-002", customer="Jane Smith", vehicle="BMW Series 3", from_date="2026-03-05", to_date="2026-03-10", status="Active"),
        Booking(booking_ref="BK-003", customer="Mike Jones", vehicle="Volkswagen Golf", from_date="2026-03-08", to_date="2026-03-12", status="Pending"),
        Booking(booking_ref="BK-004", customer="Sarah Wilson", vehicle="Audi A4", from_date="2026-03-10", to_date="2026-03-15", status="Confirmed"),
        Booking(booking_ref="BK-005", customer="Tom Brown", vehicle="Ford Focus", from_date="2026-03-12", to_date="2026-03-14", status="Active"),
    ]:
        db.session.add(bk)

    for ev in [
        CalendarEvent(date="2026-03-01", title="BK-001 Start", color="success"),
        CalendarEvent(date="2026-03-05", title="BK-001 End / BK-002 Start", color="primary"),
        CalendarEvent(date="2026-03-08", title="BK-003 Start", color="success"),
        CalendarEvent(date="2026-03-10", title="BK-002 End / BK-004 Start", color="primary"),
        CalendarEvent(date="2026-03-12", title="BK-003 End / BK-005 Start", color="success"),
        CalendarEvent(date="2026-03-14", title="BK-005 End", color="danger"),
        CalendarEvent(date="2026-03-15", title="BK-004 End", color="danger"),
        CalendarEvent(date="2026-03-20", title="Fleet Maintenance Day", color="warning"),
    ]:
        db.session.add(ev)

    for c in [
        Competitor(name="AutoRent", rating=4.2, daily_price=45, market_share=28, vehicles=120, trend="+3%"),
        Competitor(name="DriveEasy", rating=3.8, daily_price=38, market_share=18, vehicles=85, trend="-1%"),
        Competitor(name="SpeedRent", rating=4.5, daily_price=55, market_share=22, vehicles=95, trend="+5%"),
        Competitor(name="EcoRide", rating=4.0, daily_price=35, market_share=12, vehicles=60, trend="+1%"),
    ]:
        db.session.add(c)

    db.session.commit()
