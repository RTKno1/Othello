from Othello_Core import OthelloCore

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

class StudentOthello(OthelloCore):
    def __init__(self):
        pass
        
    def is_valid(self, move):
        """Is move a square on the board?"""
        if board[move] is OUTER:
            return False
        return True
    
    def opponent(self, player):
        """Get player's opponent piece."""
        if player is BLACK:
            return WHITE
        return BLACK
    
    def find_bracket(self, square, player, board, direction):
        """Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found"""
        if board[square] is EMPTY:
            square += direction
            if board[square] is EMPTY:
                return None
            while board[square] is self.opponent(player):
                square += direction
            if board[square] is player:
                return square
            return None
        else:
            square += direction
            if board[square] is EMPTY:
                return None
            while board[square] is self.opponent(player):
                square += direction
                temp = board[square]
            if board[square] is player:
                return square
            return None
        
    def is_legal(self, move, player, board):
        """Is this a legal move for the player?"""
        if board[move] is not EMPTY:
            return False
        else:
            for d in DIRECTIONS:
                if self.find_bracket(move, player, board, d) is not None:
                    return True
        return False
    ### Making moves

    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.

    def make_move(self, move, player, board):
        """Update the board to reflect the move by the specified player."""
        board[move] = player

    def make_flips(self, move, player, board, direction):
        """Flip pieces in the given direction as a result of the move by player."""
        move += direction
        while board[move] is not player:
            board[move] = player
            move += direction

    def legal_moves(self, player, board):
        """Get a list of all legal moves for player, as a list of integers"""
        li = []
        for i in self.squares():
            if self.is_legal(i, player, board):
                    li.append(i)
        if li is []:
            return None
        return li

    def any_legal_move(self, player, board):
        """Can player make any moves? Returns a boolean"""
        if self.legal_moves is not None:
            return True
        return False

    def next_player(self,board, prev_player):
        """Which player should move next?  Returns None if no legal moves exist."""
        if self.any_legal_move(self.opponent(prev_player), board) is True:
            return self.opponent(prev_player)
        elif self.any_legal_move(prev_player, board) is True:
            return prev_player
        return None

    def score(self, player, board):
        count = 0
        for i in range(11, 89):
            if board[i] is player:
                count += 1
            return count - (64 - count)
        """Compute player's score (number of player's pieces minus opponent's)."""
        pass
    def random_play(self, player, board):
        while self.next_player(board, player) is not None:
            move = self.legal_moves(player, board)[0]
            self.make_move(move, player, board)
            for d in DIRECTIONS:
                if self.find_bracket(move, player, board, d):
                    self.make_flips(move, player, board, d)
            print (self.print_board(board))
            player = self.opponent(player)
        print (self.print_board(board))
