from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class UserAddress(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    gender = db.Column(db.String(50))
    dob = db.Column(db.String(200))
    licence_no = db.Column(db.String(200))
    demerit = db.Column(db.Integer)
    address1 = db.Column(db.String(300))
    address2 = db.Column(db.String(300), nullable=True)
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zipcode = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)

    def serialize_short(self):
        return {
            'id': self.id,
            'email': self.email,
            'full_name': self.first_name + " " + self.last_name,
            "dob": self.dob,
            'licence_no': self.licence_no,
            "address": self.address1 + " " + self.address2 + ", " + self.state + " " + str(self.zipcode),
        }

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            "gender": self.gender,
            "dob": self.dob,
            'licence_no': self.licence_no,
            "address1": self.address1,
            "address2": self.address2,
            "country": self.country,
            "state": self.state,
            "zipcode": self.zipcode,
            'is_active': self.is_active
        }