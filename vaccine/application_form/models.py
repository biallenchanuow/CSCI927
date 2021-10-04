from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    given_name = db.Column(db.String(255), nullable=False)
    family_name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    indigenous_status = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    place_of_birth = db.Column(db.String(255), nullable=False)
    residential_address = db.Column(db.String(255), nullable=False)
    residence_status = db.Column(db.String(255), nullable=False)
    medicare = db.Column(db.String(255), nullable=False)
    vaccine_history = db.Column(db.String(255), nullable=False)
    work_type = db.Column(db.String(255), nullable=False)
    booker_description = db.Column(db.String(255), nullable=False)
    parking_required = db.Column(db.String(255), nullable=False)
    interpreter_required = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<application {self.id} {self.given_name}>'

    def serialize(self):
        return {
            'id': self.id,
            'given_name': self.given_name,
            'family_name': self.family_name,
            'gender': self.gender,
            'indigenous_status': self.indigenous_status,
            'age': self.age,
            'place_of_birth': self.place_of_birth,
            'residential_address': self.residential_address,
            'residence_status': self.residence_status,
            'medicare': self.medicare,
            'vaccine_history': self.vaccine_history,
            'work_type': self.work_type,
            'booker_description': self.booker_description,
            'parking_required': self.parking_required,
            'interpreter_required': self.interpreter_required
        }
