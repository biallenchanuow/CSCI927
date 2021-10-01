from flask import Flask
from routes import address_blueprint
from models import db, Address, init_app
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QabDtY3Dt_bgd76i0mP_wg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/address.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(address_blueprint)
init_app(app)

admin = Admin(app)
admin.add_view(ModelView(Address, db.session))

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=3002)
