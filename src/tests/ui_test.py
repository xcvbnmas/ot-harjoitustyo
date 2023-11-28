import unittest
import tkinter as tk
from game import TicTacToeGame
from ui import TicTacToeGrid

class TestTicTacToeGrid(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()
        self.ui = TicTacToeGrid(self.game)
        
    def test_create_buttons(self):
        self.assertEqual(len(self.ui.buttons), 3)
        self.assertEqual(len(self.ui.buttons[0]), 3)
