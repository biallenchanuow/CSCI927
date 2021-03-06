from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class Address(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(200), nullable=False)
    licence_no = db.Column(db.String(200), nullable=False)
    address1 = db.Column(db.String(300), nullable=False)
    address2 = db.Column(db.String(300), nullable=True)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<user {self.id}>'

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
            "api_key": self.api_key
        }

    def update_api_key(self):
        self.api_key = generate_password_hash(
            self.email + str(datetime.utcnow))
