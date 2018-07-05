from board import Board

# Player X will be the computer, and will always go first
def play():
    board = Board()
    while True:
        board.showBoard()
        move = int(input('Player {}, enter your move (9 to quit): '.format(board.currentPlayer)))
        if move == 9:
            print('Quit Successfully!')
            break
        if board.validMove(move):
            board.makeMove(move)
            if board.won():
                board.showBoard()
                print('Player {} won!'.format(board.currentPlayer))
                break
            if board.full():
                print('It\'s a tie!')
                break
            board.turn()
        else:
            print('Invalid move! Please try again.')

if __name__ == "__main__":
    play()