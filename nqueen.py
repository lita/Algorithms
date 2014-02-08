"""
The N Queen is the problem of placing N chess queens on an NxbN chessboard so 
that no two queens attack each other. For example, following is a solution for
4 Queen problem.
"""
class Rook(object):
    def __init__(self):
        self.name = 'R'

    def checkMovement(self, board, x, y):
        if board[x][y] == 'R':
            return False
        
        # Check horizontal and vertical
        for i in range(len(board)):
            if board[x][i] == 'R' or board[i][y] == 'R':
                return False

        return True

class Queen(object):
    def __init__(self):
        self.name = 'Q'

    def checkMovement(self, board, x, y):
        """
        Checks the diagonal paths to see if any queens
        are in the path.
        """
        
        if board[x][y] == 'Q':
            # Queen is already there
            return False
        
        # Check horizontal and vertical
        for i in range(len(board)):
            if board[x][i] == 'Q' or board[i][y] == 'Q':
                return False

        # Checks upper left
        upX, upY = x, y
        while upX >= 0 and upY >= 0:
            if board[upX][upY] == 'Q':
                return False

            upX -= 1
            upY -= 1
        
        # Checks lower left
        upX, downY = x, y
        while upX >= 0 and downY < len(board):
            if board[upX][downY] == 'Q':
                return False

            upX -= 1
            downY += 1      

        # Checks upper right
        downX, upY = x, y
        while upY >= 0 and downX < len(board):
            if board[downX][upY] == 'Q':
                return False
            upY -= 1
            downX += 1      

        # Checks lower right
        downX, downY = x, y 
        while downX < len(board) and downY < len(board):
            if board[downX][downY] == 'Q':
                return False

            downX += 1
            downY += 1
        return True

class Board(object):
    """simple board class"""
    def __init__(self, n, piece):
        self.board = [['' for i in xrange(n)] for j in xrange(n)]
        self.len = n
        self.piece = piece

    def printBoard(self):
        """prints the board"""
        board = ' '
        for x in xrange(self.len):
            board = board + "_ "
        board = board + '\n'
        for x in xrange(self.len):
            board = board + '|'
            for y in xrange(self.len):
                if self.board[x][y]:
                    board = board + self.board[x][y] + "|"
                else:
                    board = board + "_|"
            board = board + '\n'
        print board

    def placePiece(self, x, y):
        """
        Checks to see if the queen is safe to place.
        If not, returns False.
        Otherwise, places the queen in the object and returns
        True.
        Parameters:
        x - x cooridnate
        y - y coordinate
        """
        if self.piece.checkMovement(self.board, x, y):
            self.board[x][y] = self.piece.name
            return True
        return False

    def removePiece(self, x, y):
        """removes the chess piece """
        self.board[x][y] = ''    

def solveNQueen(n, piece):
    board = Board(n, piece)
    if not _solveNQueen(n, board):
        print "could not find solution"

def _solveNQueen(pieces, board):
    if pieces == 0:
        board.printBoard()
        return True

    for x in xrange(board.len):
        for y in xrange(board.len):
            if board.placePiece(x, y):
                if _solveNQueen(pieces-1, board):
                    return True
                else:
                    board.removePiece(x, y)

    return False

queen = Queen()
rook = Rook()
solveNQueen(5, queen)
solveNQueen(5, rook)
