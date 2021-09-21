from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nswavatarservice@gmail.com'
app.config['MAIL_PASSWORD'] = 'csci927project'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('COVID-19 vaccination is booked',
                  sender='nswavatarservice@gmail.com', recipients=['nswavatarservice@gmail.com'])
    msg.body = 'Hi, your COVID-19 Vaccination booking has been CONFIRMED. Please bring your Medicar card and photo ID on the day.'

    mail.send(msg)
    return "Message sent"


if __name__ == '__main__':
    app.run(debug=True, port=5004)
