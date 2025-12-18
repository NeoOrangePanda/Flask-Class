from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def get_location():
    d = request.json
    url = f'https://nominatim.openstreetmap.org/reverse?lat={d["latitude"]}&lon={d["longitude"]}&format=json'
    r = requests.get(url, headers={'User-Agent': 'SimpleApp'})
    address = r.json().get('display_name', 'Not found')
    return jsonify({"message": f"You are at: {address}"})


if __name__ == "__main__":
    app.run()