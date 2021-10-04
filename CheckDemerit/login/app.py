from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager
from routes import blueprint
from models import User, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

DB_NAME = 'user.db'

app.config['SECRET_KEY'] = 'aoeir03r'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)
app.register_blueprint(blueprint)
admin = Admin(app)
admin.add_view(ModelView(User, db.session))

# app.register_blueprint(auth, url_prefix="/")

login_manager = LoginManager()
login_manager.login_view = 'blueprint.login'
login_manager.init_app(app)

migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def create_database(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print('New Database Created')
    else:
        print('Database already exists')


create_database(app)

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)
