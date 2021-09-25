from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from routes import blueprint


app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'v8hmlqFIixw3wXp19wEisw'
app.config['WTF_CSRF_SECRET_KEY'] = 'Ln0TIVNQzkCbaJYPCdgryg'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.register_blueprint(blueprint)
admin = Admin(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_message = "Please Login."
login_manager.login_view = 'frontend.login'

bootstrap = Bootstrap(app)


@login_manager.user_loader
def load_user(user_id):
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
