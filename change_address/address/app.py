from flask import Flask, g
from routes import address_blueprint, user_blueprint
from flask.sessions import SecureCookieSessionInterface
from flask_login import LoginManager
from models import db, Address, init_app
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QabDtY3Dt_bgd76i0mP_wg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/address.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(address_blueprint)
app.register_blueprint(user_blueprint)
init_app(app)
login_manager = LoginManager(app)
admin = Admin(app)
admin.add_view(ModelView(Address, db.session))

migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return Address.query.filter_by(id=user_id).first()


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = Address.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None


class CustomSessionInterface(SecureCookieSessionInterface):
    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
