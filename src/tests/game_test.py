import unittest
from game import TicTacToeGame


class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()
             
    def test_starting_game(self):
        self.assertEqual(self.game.current, 'X')
        self.assertEqual(self.game.grid, [' '] * 9)
        
    def test_switching_player(self):
        self.assertEqual(self.game.current, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current, 'X')
