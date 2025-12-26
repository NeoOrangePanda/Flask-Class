from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"

db_path = 'Class Work\Login App\users.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, email TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginaction', methods=['POST'])
def login_action():
    username = request.form['username-input']
    password = request.form['password-input']

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username and password')
        return redirect(url_for('home'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registeraction', methods=['POST'])
def register_action():
    username = str(request.form['username-input'])
    email = str(request.form['email-input'])
    password = str(request.form['password-input'])

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    existing_user = cursor.fetchone()

    if existing_user:
        flash('User already exists!')
        return redirect(url_for('home'))
    else:
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=24011)