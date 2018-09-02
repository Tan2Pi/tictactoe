from board import Board
from copy import deepcopy
from math import inf


# def miniMax(node):
#     if node.board.currentPlayer == 'X':
#         if node.board.won():
#             node.rank = 1
#         elif node.board.full():
#             node.rank = 0
#         else:
#             for child in node.children:
#                 node.rank = miniMax(child)
#     else:
#         if node.board.won():
#             node.rank = -1
#         elif node.board.full():
#             node.rank = 0
#         else:
#             for child in node.children:
#                 node.rank = miniMax(child)


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
    if depth == 0 or board.state():
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

def alphabeta(board, depth, alpha, beta):
    if depth == 0 or board.state():
        if board.won('O'):
            score = 1
        elif board.won('X'):
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
            optimum = max(optimum, alphabeta(maxBoard, depth-1, alpha, beta), key = lambda s: s['score'])
            optimum['i'] = i
            alpha = max(alpha, optimum['score'])
            if alpha >= beta:
                break
        return optimum
    else:
        optimum = {'score': +inf, 'i': -1}
        for i in board.empty_spaces():
            minBoard = deepcopy(board)
            minBoard.makeMove(i)
            minBoard.turn()
            optimum = min(optimum, alphabeta(minBoard, depth-1, alpha, beta), key = lambda s: s['score'])
            optimum['i'] = i
            beta = min(beta, optimum['score'])
            if alpha >= beta:
                break
        return optimum