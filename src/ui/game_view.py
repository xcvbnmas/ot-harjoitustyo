import tkinter as tk
from tkinter import messagebox

class TicTacToeGrid(tk.Tk):
    """Luokka, joka vastaa ristinolla-pelin näkymästä"""

    def __init__(self, game):
        """Luokan konstruktori, joka luo pelin näkymän
        Args:
            game: vastaa pelin toiminnasta

        """
        super().__init__()
        self.title("Ristinolla")
        self.create_grid()
        self.game = game
        self.resizable(False, False)

    def create_grid(self):
        """Metodi, jonka avulla ruudukko luodaan"""

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self, font=('Arial', 20), width=10, height=5, 
                                   command=lambda i=i, j=j: self.click_button(i, j))
                button.grid(row=i, column=j, sticky='nsew')
                row.append(button)
            self.buttons.append(row)

        exit_game_button = tk.Button(self, text="Exit game", command=self.exit_game)
        exit_game_button.grid(row=3, column=1, sticky='nsew')

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def click_button(self, i, j):
        """Metodi, joka vastaa ruutuun merkitsemisestä/napin painamisesta
        ja siitä seuraavasta vuoron vaihdosta tai viestistä
        
        Args:
            i, j: ruudun koordinaatit
        """
        if self.game.play(i, j):
            self.buttons[i][j].config(text=self.game.current, state='disabled')
            if self.game.winner():
                messagebox.showinfo("Ristinolla", f"{self.game.current} voittaa")
                self.game.reset_game()
                self.reset_grid()
            elif ' ' not in self.game.grid:
                messagebox.showinfo("Ristinolla", "Tasapeli")
                self.game.reset_game()
                self.reset_grid()
            else:
                self.game.switch_player()

    def reset_grid(self):
        """Metodi, jonka avulla ruudukko luodaan uudestaan uutta peliä varten"""

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state='normal')

    def exit_game(self):
        """Metodi, joka sulkee pelin näkymän"""
        self.destroy()
