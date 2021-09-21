from flask import Flask
from route import schedule_blueprint
from model import db, Schedule, init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ugKWzXj1YFtioYsh-wJ9hw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(schedule_blueprint)
init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
