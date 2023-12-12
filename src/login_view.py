import tkinter as tk
from tkinter import ttk, constants, messagebox
import sqlite3

class LoginView:
    """Luokka, joka vastaa käyttäjän kirjautumisen näkymästä"""

    def __init__(self, root, show_register_view, start_game):
        self.root = root
        self.show_register_view = show_register_view
        self.start_game = start_game
        self.frame = ttk.Frame(master=self.root)
        self.initialize()

    def initialize(self):
        """Luo näkymän sisäänkirjautumiselle"""

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self.root, text="Register", command=self.show_register_view)
        self.register_button.pack()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def login(self):
        """Kirjaa käyttäjän sisään, tai näyttää virheviestin käyttäjälle,
        joka yrittää kirjautua olemattomalla käyttäjätunnuksella/salasanalla

        """

        username = self.username_entry.get()
        password = self.password_entry.get()

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        connection.close()

        if user:
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("Error", "Invalid username or password")
        
        self.start_game()

    def show_register_view(self):
        self.show_register_view()