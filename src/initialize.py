from database_connection import get_database_connection

def initialize_database():
    """Metodi, joka luo tietokantataulun käyttäjille"""

    connection = get_database_connection()

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
