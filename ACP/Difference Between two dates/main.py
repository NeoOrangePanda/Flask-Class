from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        date1 = datetime.strptime(str(request.form.get('first-date-input')), '%d/%m/%Y')
        date2 = datetime.strptime(str(request.form.get('second-date-input')), '%d/%m/%Y')

        difference = date2 - date1
        return render_template('index.html', days=difference.days)
    except Exception as e:
        return render_template('error.html', error_msg=e)

if __name__ == "__main__":
    app.run(debug=True, port=24011)