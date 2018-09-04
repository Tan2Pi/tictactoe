from board import Board
from minimax import *
from copy import deepcopy
from math import inf

class Game:
    def computerPlayer(self, player):
        move = alphabeta(deepcopy(self.board.board), self.board.depth(), -inf, +inf, player)
        self.board.makeMove(Board.conversion[(move['i'],move['j'])])
    
    def humanPlayer(self):
        while True:
            move = int(input('Player {}, enter your move (9 to quit): '.format(self.board.currentPlayer)))
            if move == 9:
                print('Quit Successfully!')
                self.playing = False
                break
            elif self.board.validMove(move):
                self.board.makeMove(move)
                break
            else:
                print('Invalid move! Please try again.')

    def menu(self):
        while True:
            option = int(input('(1) Human vs. Human\n(2) Human vs. Computer\n(3) Exit\nPick a game option: '))
            if option > 3 or option < 1:
                print('Invalid input! Please try again.')
            else:
                if option == 1:
                    self.board = Board()
                    self.playing = True
                    self.multiPlayer()
                elif option == 2:
                    self.board = Board()
                    self.playing = True
                    self.singlePlayer()
                else:
                    break
    
    def singlePlayer(self):
        while self.playing:
            self.board.show()
            if self.board.currentPlayer == 'O':
                print('Player O is thinking...')
                self.computerPlayer()
                if self.board.won():
                    self.board.show()
                    print('Player {} won!'.format(self.board.currentPlayer))
                    break
                elif self.board.full():
                    self.board.show()
                    print('It\'s a tie!')
                    break
                else:
                    self.board.turn()
            else:
                self.humanPlayer()
                if self.board.won():
                    print('Player {} won!'.format(self.board.currentPlayer))
                    break
                elif self.board.full():
                    print('It\'s a tie!')
                    break
                else:
                    self.board.turn()

    def multiPlayer(self):
        while self.playing:
            self.board.show()
            self.humanPlayer()
            if self.board.won():
                print('Player {} won!'.format(self.board.currentPlayer))
                break
            elif self.board.full():
                print('It\'s a tie!')
                break
            else:
                self.board.turn()

            
if __name__ == "__main__":
    game = Game()
    game.menu()