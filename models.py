from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")

    def to_dict(self):
        return {"id": self.id, "username": self.username, "role": self.role}


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="New")

    def to_dict(self):
        return {"id": self.id, "from": self.from_email, "subject": self.subject,
                "date": self.date, "status": self.status}


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    plate = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Available")
    cls = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {"id": self.id, "make": self.make, "model": self.model,
                "plate": self.plate, "status": self.status, "cls": self.cls,
                "year": self.year, "mileage": self.mileage}


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(40), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "city": self.city,
                "address": self.address, "phone": self.phone,
                "lat": self.lat, "lng": self.lng}


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_ref = db.Column(db.String(20), unique=True, nullable=False)
    customer = db.Column(db.String(100), nullable=False)
    vehicle = db.Column(db.String(100), nullable=False)
    from_date = db.Column(db.String(20), nullable=False)
    to_date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")

    def to_dict(self):
        return {"id": self.id, "booking_ref": self.booking_ref, "customer": self.customer,
                "vehicle": self.vehicle, "from_date": self.from_date,
                "to_date": self.to_date, "status": self.status}


class CalendarEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(20), nullable=False, default="primary")

    def to_dict(self):
        return {"id": self.id, "date": self.date, "title": self.title, "color": self.color}


class Competitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    daily_price = db.Column(db.Integer, nullable=False)
    market_share = db.Column(db.Integer, nullable=False)
    vehicles = db.Column(db.Integer, nullable=False)
    trend = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "rating": self.rating,
                "dailyPrice": self.daily_price, "marketShare": self.market_share,
                "vehicles": self.vehicles, "trend": self.trend}
