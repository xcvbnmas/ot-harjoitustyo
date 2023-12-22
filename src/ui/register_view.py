import tkinter as tk
from tkinter import ttk, messagebox, constants
from repositories.user_repository import UserRepository

class RegisterView:
    """Luokka, joka vastaa uuden käyttäjän rekisteröitymisestä eli uuden käyttäjän luomisesta"""

    def __init__(self, root, show_login_view):
        self.root = root
        self.show_login_view = show_login_view
        self.frame = ttk.Frame(master=self.root)
        self.user_repository = UserRepository()
        self.initialize()

    def initialize(self):
        """Luo näkymän rekisteröitymiselle"""

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
        """Lisää uuden käyttäjän tietokantaan, tai näyttää virheviestin käyttäjälle,
        joka yrittää rekisteröityä jo olemassa olevalla käyttäjätunnuksella

        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        existing_user = self.user_repository.find_user_by_username(username)

        if existing_user:
            messagebox.showerror("Error", "Username already taken")
        else:
            self.user_repository.create_user(username, password)
            messagebox.showinfo("Success", "Registration successful")

    def show_login_view(self):
        self.show_login_view()
