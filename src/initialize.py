import sqlite3

def initialize_database():
    """Metodi, joka luo tietokantataulun käyttäjille"""

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()