from flask import Flask, request, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)
db = 'Class Work\Shopping Cart Contest\database.db'

def get_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            phoneNumber TEXT,
            numberOfItems INTEGER,
            totalAmount INTEGER,
            currentDate TEXT
        );
    """)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details', methods=['POST'])
def details():
    username = request.form['user_name']
    phoneNumber = request.form['contact_number']
    numberOfItems = request.form['number_of_items']
    totalAmount = request.form['amount']
    currentDate = request.form['current_date']

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO customers (username, phoneNumber, numberOfItems, totalAmount, currentDate) VALUES (?, ?, ?, ?, ?);
    """, (username, phoneNumber, numberOfItems, totalAmount, currentDate))
    conn.commit()
    conn.close()
    
    return render_template('winner.html')

@app.route('/winner')
def winner():
    today = datetime.now().strftime('%Y-%m-%d')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT username, phoneNumber FROM customers WHERE currentDate = ? ORDER BY totalAmount DESC LIMIT 1;
    """, (today,))
    row = cur.fetchone()

    if row:
        return render_template('winner.html', user_name = row['username'], phone_number = row['phoneNumber'])

    return render_template('winner.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)