from board import *
from copy import deepcopy
from math import inf

# https://en.wikipedia.org/wiki/Minimax
def miniMax(board, depth):
    if depth == 0 or board.state():
        if board.currentPlayer == 'O' and board.won():
            score = 10
        elif board.currentPlayer == 'X' and board.won():
            score = -10
        else:
            score = 0
        return {'score': score, 'i': -1}
    
    if board.currentPlayer == 'O':
        optimum = {'score': -inf, 'i': -1}
        for i in board.empty_spaces():
            maxBoard = deepcopy(board)
            maxBoard.makeMove(i)
            maxBoard.turn()
            value = miniMax(maxBoard, depth-1)
            value['i'] = i
            optimum = max(optimum, value, key = lambda s: s['score'])
        return optimum
    else:
        optimum = {'score': +inf, 'i': -1}
        for i in board.empty_spaces():
            minBoard = deepcopy(board)
            minBoard.makeMove(i)
            minBoard.turn()
            value = miniMax(minBoard, depth-1)
            value['i'] = i
            optimum = min(optimum, value, key = lambda s: s['score'])
        return optimum


# https://en.wikipedia.org/wiki/Alpha–beta_pruning
def alphabeta(board, depth, alpha, beta, player):
    if depth == 0 or state(board):
        if won(board, 'O'):
            score = 10
        elif won(board, 'X'):
            score = -10
        else:
            score = 0
        return {'score': score, 'i': -1, 'j': -1}
    
    if player == 'O':
        optimum = {'score': -inf, 'i': -1, 'j': -1}
        for square in empty_squares(board):
            i, j = square[0], square[1]
            board[i][j] = player
            value =  alphabeta(board, depth-1, alpha, beta, 'X')
            value['i'], value['j'] = i, j
            optimum = max(optimum, value, key = lambda s: s['score'])
            board[i][j] = ' '
            alpha = max(alpha, optimum['score'])
            if alpha >= beta:
                break
    else:
        optimum = {'score': +inf, 'i': -1, 'j': -1}
        for square in empty_squares(board):
            i, j = square[0], square[1]
            board[i][j] = player
            value =  alphabeta(board, depth-1, alpha, beta, 'O')
            value['i'], value['j'] = i, j
            optimum = min(optimum, value, key = lambda s: s['score'])
            board[i][j] = ' '
            beta = min(beta, optimum['score'])
            if alpha >= beta:
                break
    
    return optimum