from game import TicTacToeGame
from ui import TicTacToeGrid

if __name__ == "__main__":
    game = TicTacToeGame()
    app = TicTacToeGrid(game)
    app.mainloop()
