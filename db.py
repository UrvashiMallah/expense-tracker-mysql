import mysql.connector
from config import DB_CONFIG

conn = None

def create_connection():
    global conn
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            description VARCHAR(255),
            amount FLOAT,
            date DATE
        )
    """)
    conn.commit()

def insert_expense(description, amount, date):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s)", (description, amount, date))
    conn.commit()

def fetch_expenses():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    return cursor.fetchall()