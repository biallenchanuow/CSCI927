from flask import Flask
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager
from change_address.models import UserAddress, db
from change_address.routes import blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

DB_NAME = 'address.db'

app.config['SECRET_KEY']='jkldsa923'
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
db.init_app(app)
app.register_blueprint(blueprint)
admin = Admin(app)
admin.add_view(ModelView(UserAddress, db.session))

migrate = Migrate(app, db)


def create_database(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print('New Database Created')
    else:
        print('Database already exists')


create_database(app)

if __name__ == '__main__':
    app.run(debug=True, port=5004)