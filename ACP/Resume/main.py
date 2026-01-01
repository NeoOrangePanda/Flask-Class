from flask import Flask, render_template, request, Blueprint, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "app_secret_keys"

def get_db_connection():
    conn = sqlite3.connect('ACP\Resume\info.db')
    return conn

@app.route('/')
def home():
    selected_set = 'set1'

    conn = get_db_connection()
    info_set = conn.execute('SELECT name, email, task, phone_num FROM resume_info WHERE setID = ?', (selected_set,)).fetchone()

    splited_name = str(info_set[0]).split()

    return render_template('index.html', info_set=info_set, s=splited_name)

if __name__ == "__main__":
    app.run(debug=True)