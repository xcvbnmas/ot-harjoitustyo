from database_connection import get_database_connection
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.connection = get_database_connection()
        self.user_repository = UserRepository()

    def register_user(self, username, password):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            raise Exception("Username already taken")

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.connection.commit()

    def login(self, username, password):
        user = self.user_repository.find_user(username, password)
        return user
