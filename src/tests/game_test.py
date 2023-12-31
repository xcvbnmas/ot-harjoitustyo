import unittest
from game import TicTacToeGame


class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()
             
    def test_start_game(self):
        self.assertEqual(self.game.current, 'X')
        self.assertEqual(self.game.grid, [' '] * 9)
        
    def test_switch_player(self):
        self.assertEqual(self.game.current, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current, 'X')

    def test_reset_game(self):
        self.game.current = 'O'
        self.game.grid = ['O', 'X', 'O', ' ', 'X', ' ', 'X', 'O', ' ']
        self.game.reset_game()
        self.assertEqual(self.game.current, 'X')
        self.assertEqual(self.game.grid, [' '] * 9)

    def test_play(self):
        result = self.game.play(0, 0)
        self.assertTrue(result)
        self.assertEqual(self.game.current, 'X')
        self.assertEqual(self.game.grid[0], 'X')

    def test_winner(self):
        self.game.grid = ['X', 'X', 'X', ' ', 'O', 'O', ' ', ' ', ' ']
        result = self.game.winner()
        self.assertTrue(result)

        self.game.grid = ['X', 'O', ' ', 'X', 'O', ' ', 'X', ' ', ' ']
        result = self.game.winner()
        self.assertTrue(result)

        self.game.grid = ['O', 'X', ' ', 'X', 'O', ' ', ' ', ' ', 'O']
        result = self.game.winner()
        self.assertTrue(result)

        self.game.grid = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        result = self.game.winner()
        self.assertFalse(result)