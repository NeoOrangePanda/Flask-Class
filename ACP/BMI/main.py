from flask import render_template, Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        weight = float(request.form.get('weight-input'))
        height = float(request.form.get('height-input'))

        bmi = round(weight / (height ** 2), 3)

        status = ()

        if bmi < 18.5:
            status = ("Underweight", "#1269ff")
        elif bmi >= 18.5 and bmi <= 24.9:
            status = ("Normal", "#0c8711")
        elif bmi >= 25 and bmi <= 29.9:
            status = ("Overweight", "#FFC107")
        elif bmi >= 30 and bmi <= 34.9:
            status = ("Obese Class I", "#FF9800")
        elif bmi >= 35 and bmi <= 39.9:
            status = ("Obese Class II", "#EE3528")
        elif bmi >= 40:
            status = ("Obese Class III", "#8315A1")

        return render_template('index.html', bmi=bmi, status=status[0], status_color=status[1])
    except ValueError:
        return """
            <p>Please enter valid inputs</p>
        """

if __name__ == "__main__":
    app.run(debug=True, port=24011)