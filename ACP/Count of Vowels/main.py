from flask import Flask, render_template, request
import re

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

    highlighted = re.sub(r'([aeiouAEIOU])', r'<span class="text-green-500">\1</span>', string)

    for letter in string_modified:
        if letter in vowels:
            v_count += 1

    return render_template('index.html', v_count=v_count, s=highlighted)

if __name__ == "__main__":
    app.run(debug=True, port=24011)