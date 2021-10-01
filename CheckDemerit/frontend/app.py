from flask import Flask
from frontend.routes import blueprint

app = Flask(__name__)
app.config['SECRET_KEY']='njkd93r2k'
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)