class TicTacToeGame:
    """Luokka, joka vastaa pelin toiminnasta"""

    def __init__(self):
        """Luokan konstruktori"""

        self.grid = [' '] * 9
        self.current = 'X'

    def play(self, i, j):
        """ Merkkaa ruutuun (i,j) joko merkin X tai O
        Args:
            i ja j: ruudun koordinaatit
        """
        if self.grid[i * 3 + j] == ' ':
            self.grid[i * 3 + j] = self.current
            return True
        return False

    def winner(self):
        """ Määrittää pelin voittajan"""

        # tähän on käytetty apuna ChatGPT
        for i in range(3):
            if self.grid[i * 3] == self.grid[i * 3 +1] == self.grid[i * 3 + 2] != ' ':
                return True
            if self.grid[i] == self.grid[i + 3] == self.grid[i + 6] != ' ':
                return True
        if self.grid[0] == self.grid[4] == self.grid[8] != ' ' or \
            self.grid[2] == self.grid[4] == self.grid[6] != ' ':
            return True
        return False
        # tähän loppuu koodi, johon käytetty apuna ChatGPT

    def switch_player(self):
        """ Vaihtaa vuoron pelaajalta toiselle"""

        if self.current == 'X':
            self.current = 'O'
        else:
            self.current = 'X'

    def reset_game(self):
        """ Aloittaa pelin alusta"""

        self.grid = [' '] * 9
        self.current = 'X'
