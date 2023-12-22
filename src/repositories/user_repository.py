from database_connection import get_database_connection

class UserRepository:
    def __init__(self):
        self.connection = get_database_connection()

    def create_user(self, username, password):
        """Metodi, joka lisää käyttäjän tietokantaan"""
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
        finally:
            cursor.close()

    def find_user_by_username(self, username):
        """Metodi, joka etsii käyttäjänimen (käytetään rekisteröinnissä 
        tarkistamaan, onko käyttäjänimeä jo olemassa)"""
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            return cursor.fetchone()
        finally:
            cursor.close()

    def find_user(self, username, password):
        """Metodi, joka etsii käyttäjän ja salasanan tietokannasta
        (käytetään kirjautumisessa)"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        return user
