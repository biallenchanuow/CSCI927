from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(255), unique=True)
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<user {self.id}, {self.username}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'is_admin': self.is_admin,
            'api_key': self.api_key,
            'is_active': self.is_active,
        }

    def update_api_key(self):
        self.api_key = generate_password_hash(
            self.username + str(datetime.utcnow))
