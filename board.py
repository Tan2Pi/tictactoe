# class Player:
#     __init__(self, player = ' '):
#         self.player = player
    

class Board:
    size = 3

    def __init__(self):
        self.board = [([' ']*Board.size) for row in range(Board.size)]
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
    
    def turn(self):
        Os = len(filter(lambda o: o == 'O', self.flatBoard))
        Xs = len(filter(lambda x: x == 'X', self.flatBoard))
        if Ox <= Xs:
           self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
    
    def diag(board):
        return [board[n][n] for n in range(0,Board.size)]

    def rdiag(board):
        return diag(transpose(board))
    
    def transpose(board): 
        return [*zip(*board)]
    
    def winRow(self,board,row,col):
        if board[row][col] == self.currentPlayer:
            if (col == Board.size - 1):
                return True
            else:
                return winRow(row,col+1)
        else:
            return False
    
    def won(self):
        for i in range(Board.size):
            if self.winRow(self.board,i,0):
                return True
        for i in range(Board.size):
            if self.winRow(transpose(self.board),i,0):
                return True
        if self.winRow(diag(self.board),0,0):
            return True
        elif self.winRow(rdiag(self.board),0,0):
            return True
        else:
            return False
    
    def validMove(self,move):
        if move >= 0 and move <= Board.size*Board.size and self.flatBoard[move] == ' ':
            return True
        else:
            return False
    
    def makeMove(self,move):
        counter = 0
        for i in range(Board.size):
            for j in range(Board.size):
                if counter == move:
                    board[i][j] = self.currentPlayer
                else:
                    counter += 1

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

# General purpose functions


if __name__ == "__main__":
    board = Board()
    board.showBoard()

    
