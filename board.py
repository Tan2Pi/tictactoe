from copy import deepcopy
    

class Board:
    size = 3

    def __init__(self):
        self.board = [([' ']*Board.size) for row in range(Board.size)]
        self.flatBoard = [x for y in self.board for x in y]
        self.currentPlayer = 'X'

    def __deepcopy__(self):
        _copy = Board()
        _copy.board = self.board
        _copy.currentPlayer = self.currentPlayer
        _copy.flatBoard = self.flatBoard
        return _copy

    def copy(self):
        copyBoard = self.board
        return copyBoard
    
    def updateBoard(self):
        self.board = [self.flatBoard[x:x+Board.size] for x in range(0, Board.size**2, Board.size)]
    
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
    
    def turn(self):
        Os = len(list(filter(lambda o: o == 'O', self.flatBoard)))
        Xs = len(list(filter(lambda x: x == 'X', self.flatBoard)))
        if Os < Xs:
           self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
    
    def winRow(self,boardRow):
        
        if len(list(filter(lambda p: p == self.currentPlayer, boardRow))) == 3:
            return True
        else:
            return False
        
    
    def won(self):
        # Checks rows
        for i in range(Board.size):
            if self.winRow(self.board[i]):
                return True
        # Checks columns
        for i in range(Board.size):
            if self.winRow(transpose(self.board)[i]):
                return True
        # Checks left diagonal
        if self.winRow(diag(self.board)):
            return True
        # Checks right diagonal
        elif self.winRow(rdiag(self.board)):
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
    
    def showBoard(self):
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


    
