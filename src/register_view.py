import tkinter as tk
from tkinter import ttk, messagebox, constants
import sqlite3

class RegisterView:
    def __init__(self, root, show_login_view):
        self.root = root
        self.show_login_view = show_login_view
        self.frame = ttk.Frame(master=self.root)
        self.initialize()

    def initialize(self):
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self.root, text="Register", command=self.register)
        self.register_button.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.show_login_view)
        self.login_button.pack()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "Username already taken")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Registration successful")

    def show_login_view(self):
        self.show_login_view()