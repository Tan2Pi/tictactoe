from board import *
from copy import deepcopy
from math import inf



# def miniMax(board, depth):

#     if board.currentPlayer == 'O':
#         optimal = {'score': -inf, 'i': 0}
#     else:
#         optimal = {'score': +inf, 'i': 0}

#     if depth == 0 or board.state():
#         if board.currentPlayer == 'O' and board.won():
#             score = 1
#         elif board.currentPlayer == 'X' and board.won():
#             score = -1
#         else:
#             score = 0
#         return {'score': score, 'i': 0}
    
#     for i in board.empty_spaces():
#         board.makeMove(i)
#         board.turn()
#         rank = miniMax(board, depth-1)
#         board.flatBoard[i] = ' '
#         board.turn()
#         rank['i'] = i

#         if board.currentPlayer == 'O':
#             if rank['score'] > optimal['score']:
#                 optimal = rank
#         else:
#             if rank['score'] < optimal['score']:
#                 optimal = rank
    
#     return optimal

            
def miniMax(board, depth):
    if depth == 0 or state(board):
        if board.currentPlayer == 'O' and board.won():
            score = 1
        elif board.currentPlayer == 'X' and board.won():
            score = -1
        else:
            score = 0
        return {'score': score, 'i': -1}
    
    if board.currentPlayer == 'O':
        optimum = {'score': -inf, 'i': -1}
        for i in board.empty_spaces():
            maxBoard = deepcopy(board)
            maxBoard.makeMove(i)
            maxBoard.turn()
            optimum = max(optimum, miniMax(maxBoard, depth-1), key = lambda p: p['score'])
        return optimum
    else:
        optimum = {'score': +inf, 'i': -1}
        for i in board.empty_spaces():
            minBoard = deepcopy(board)
            minBoard.makeMove(i)
            minBoard.turn()
            optimum = min(optimum, miniMax(minBoard, depth-1), key = lambda p: p['score'])
        return optimum

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