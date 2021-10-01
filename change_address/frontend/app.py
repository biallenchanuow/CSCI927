from flask import Flask
from flask_bootstrap import Bootstrap
from routes import blueprint

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'v8hmlqFIixw3wXp19wEisw'
app.config['WTF_CSRF_SECRET_KEY'] = 'Ln0TIVNQzkCbaJYPCdgryg'
app.config['UPLOAD_FOLDER'] = 'static'
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
