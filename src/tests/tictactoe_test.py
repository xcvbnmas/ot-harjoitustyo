import unittest
import tkinter as tk
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_tictactoe(self):
        root = tk.Tk()
        grid = TicTacToe(root)
        self.assertIsInstance(grid.buttons, list)


