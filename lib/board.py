class Board:
    def __init__(self):
        self.board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    
    def play(self, position):
        try:
            if self.piece(position) != '.':
                return False
            piece = self.find_next_player_position()
            self.board[position] = piece
            return True
        except IndexError:
            return False
    
    def find_next_player_position(self):
        o = self.board.count('o')
        x = self.board.count('x')
        if x == o:
            return 'x'
        return 'o'

    def piece(self, position):
        return self.board[position]

    def full_board(self):
        return self.board
