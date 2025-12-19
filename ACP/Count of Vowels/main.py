from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    string = str(request.form.get('string-input'))
    string_modified = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    v_count = 0

    for letter in string_modified:
        if letter in vowels:
            v_count += 1

    return render_template('index.html', v_count=v_count, s=string)

if __name__ == "__main__":
    app.run(debug=True, port=24011)