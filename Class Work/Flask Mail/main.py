from flask import Flask, render_template, request
from flask_mail import *
from random import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'h.codingal@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

otp = randint(111111, 999999)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify', methods=['POST'])
def verification():
    email = request.form['email']
    msg = Message('OTP', sender='test@test.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)

    return render_template('page.html')

@app.route('/validate', methods=['POST'])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3>Email Verification is successful</h3>"
    else:
        return "<h3>Verification failed. OTP doesn't match</h3>"

if __name__ == "__main__":
    app.run(debug=True)