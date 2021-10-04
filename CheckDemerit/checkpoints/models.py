from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class UserDemerit(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    dob = db.Column(db.String(200))
    gender = db.Column(db.String(50))
    licence_no = db.Column(db.String(200))
    demerit = db.Column(db.Integer)
    address1 = db.Column(db.String(300))
    address2 = db.Column(db.String(300), nullable=True)
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zipcode = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'full_name': self.first_name + " " + self.last_name,
            "dob": self.dob,
            "gender": self.gender,
            'licence_no': self.licence_no,
            "address": self.address1 + ", " + self.address2 + ", " + self.state + " " + str(self.zipcode),
            'demerit': self.demerit,
            "is_active": self.is_active
        }