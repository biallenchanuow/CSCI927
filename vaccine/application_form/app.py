from flask import Flask
from routes import application_blueprint
from models import db, Application, init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QzkgdKLNcM1sHZ1pyoJyOA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/application.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(application_blueprint)
init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
