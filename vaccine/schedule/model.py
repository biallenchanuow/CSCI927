from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    vaccination_cite = db.Column(db.String(255), nullable=False)
    first_slot = db.Column(db.String(255), nullable=False)
    second_slot = db.Column(db.String(255), nullable=False)
    medical_condition = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<schedule {self.id} {self.name}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'city': self.city,
            'vaccination_cite': self.vaccination_cite,
            'first_slot': self.first_slot,
            'second_slot': self.second_slot,
            'medical_condition': self.medical_condition,
        }
