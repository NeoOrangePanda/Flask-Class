from flask import render_template, request, Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checking', methods=['POST'])
def checking():
    try:
        year = int(request.form.get('year'))
        if year % 4 == 0:
            return render_template('index.html', year=year, isLeapYear=True)
        else:
            return render_template('index.html', year=year, isLeapYear=False)
    except ValueError:
        return render_template('index.html', error="Please enter a valid number")

if __name__ == "__main__":
    app.run(debug=True, port=24011)