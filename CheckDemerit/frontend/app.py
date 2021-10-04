from flask import Flask
from flask_login import LoginManager
from routes import blueprint

app = Flask(__name__)
app.config['SECRET_KEY']='njkd93r2k'
app.register_blueprint(blueprint)
login_manager = LoginManager()
# login = LoginManager(app)
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)