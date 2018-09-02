from copy import deepcopy
    

class Board:
    size = 3

    conversion = {(0,0): 0, (0,1): 1, (0,2): 2,
                  (1,0): 3, (1,1): 4, (1,2): 5,
                  (2,0): 6, (2,1): 7, (2,2): 8}

    def __init__(self):
        self.board = [([' ']*Board.size) for row in range(Board.size)]
        self.flatten()
        self.currentPlayer = 'X'

    def __deepcopy__(self, memo):
        _copy = Board()
        _copy.board = deepcopy(self.board)
        _copy.flatBoard = deepcopy(self.flatBoard)
        _copy.currentPlayer = deepcopy(self.currentPlayer)
        return _copy

    def copy(self):
        copyBoard = self.board
        return copyBoard
    
    def updateBoard(self):
        self.board = [self.flatBoard[x:x+Board.size] for x in range(0, Board.size**2, Board.size)]

    def flatten(self):
        self.flatBoard = [x for y in self.board for x in y]
    
    def full(self):
        for item in self.flatBoard:
            if item == ' ':
                return False
        return True

    def empty(self):
        for item in self.flatBoard:
            if item != ' ':
                return False
        return True
    
    def empty_spaces(self):
        spaces = []
        for i in range(0,Board.size**2):
            if self.flatBoard[i] == ' ':
                spaces.append(i)
        return spaces


    def turn(self):
        Os = len(list(filter(lambda o: o == 'O', self.flatBoard)))
        Xs = len(list(filter(lambda x: x == 'X', self.flatBoard)))
        if Os < Xs:
           self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
    
    def depth(self):
        return len(self.empty_spaces())

    def state(self):
        if self.won('X') or self.won('O') or self.full():
            return True
        else:
            return False

    def winRow(self,boardRow,player=None):
        if player == None:
            player = self.currentPlayer
        
        if len(list(filter(lambda p: p == player, boardRow))) == 3:
            return True
        else:
            return False
        

    def won(self,player=None):
        # Checks rows
        if player == None:
            player = self.currentPlayer

        for i in range(Board.size):
            if self.winRow(self.board[i],player):
                return True
        # Checks columns
        for i in range(Board.size):
            if self.winRow(transpose(self.board)[i],player):
                return True
        # Checks left diagonal
        if self.winRow(diag(self.board),player):
            return True
        # Checks right diagonal
        elif self.winRow(rdiag(self.board),player):
            return True
        else:
            return False

    def winOrDraw(self):
        if self.won():
            print('Player {} won!'.format(self.board.currentPlayer))
            return True
        elif self.full():
            print('It\'s a tie!')
            return True
        else:
            return False
            
    
    def validMove(self,move):
        if move >= 0 and move <= Board.size*Board.size and self.flatBoard[move] == ' ':
            return True
        else:
            return False

    def makeMove(self,move):
        self.flatBoard[move] = self.currentPlayer
        self.updateBoard()
        

    def showRow(self,row):
        for col in range(Board.size):
            if col == 0:
                print(' ', end='')
            if col == 1:
                print(' | ', end='')
            print(self.board[row][col], end='')
            if col == 1:
                print(' | ', end='')
            if col == 2:
                print('\n', end='')
    
    def show(self):
        for row in range(Board.size):
            if row == 1 or row == 2:
                print('-----------')
            self.showRow(row)


# Board helper functions


def diag(board):
    return [board[n][n] for n in range(0,Board.size)]

def rdiag(board):
    return diag(transpose(board))
    
def transpose(board): 
    return [*zip(*board)]


def rowWin(boardRow, player):
    if len(list(filter(lambda p: p == player, boardRow))) == 3:
            return True
    else:
        return False

def won(board, player,size=3):
    for i in range(size):
            if rowWin(board[i],player):
                return True
        # Checks columns
    for i in range(size):
        if rowWin(transpose(board)[i],player):
            return True
        # Checks left diagonal
    if rowWin(diag(board),player):
            return True
        # Checks right diagonal
    elif rowWin(rdiag(board),player):
        return True
    else:
        return False

def empty_squares(board,size=3):
    squares = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                squares.append((i,j))
    
    return squares

def state(board):
    if won(board, 'X') or won(board, 'O') or len(empty_squares(board)) == 0:
        return True
    else:
        return False
