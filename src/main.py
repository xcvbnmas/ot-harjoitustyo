import tkinter as tk
from initialize import initialize_database
from login_view import LoginView
from register_view import RegisterView
from game_view import TicTacToeGrid
from game import TicTacToeGame

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("Ristinolla")
        initialize_database()
        self.show_login_view()

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginView(
            self.root,
            self.show_register_view,
            self.start_game
        )

        self.current_view.pack()

    def show_register_view(self):
        self.hide_current_view()

        self.current_view = RegisterView(
            self.root,
            self.show_login_view
        )

        self.current_view.pack()

    # En saanut tätä metodia toimimaan kurssimateriaalin ohjeilla
    # joten käytetty apuna ChatGPT
    def hide_current_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    # tähän loppuu koodi, jossa käytetty apuna ChatGPT

    def start_game(self):
        self.hide_current_view()
        game = TicTacToeGame()  
        self.current_view = TicTacToeGrid(game)

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()