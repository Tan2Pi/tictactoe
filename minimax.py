from board import Board
from copy import deepcopy
from math import inf

# class GameNode:
#     def __init__(self, board):
#         self.board = board
#         self.children = []
    
#     def addChild(self, obj):
#         self.children.append(obj)

# class GameTree:
#     depth = 9
#     def __init__(self, board):
#         self.refresh(board)

#     def moves(self, node):
#         for i in range(Board.size**2):
#             if node.board.validMove(i):
#                 newBoard = deepcopy(node.board)
#                 newBoard.makeMove(i)
#                 newBoard.turn()
#                 newNode = GameNode(newBoard)
#                 newNode.depth = 1 + node.depth
#                 while not newNode.board.full():
#                     self.moves(newNode)
#                 node.addChild(newNode)
                

    
#     # def depthFirst(self, node):
#     #     for child in self.root.children:
#     #         if child.board == node.board:
#     #             return child
#     #         else:
#     #             self.depthFirst(child.children)

#     def refresh(self, board):
#         self.root = GameNode(board)
#         self.moves(self.root)
        
    
#     def bestMove(self):
#         miniMax(self.root)
#         bestMove = max(self.root.children, key = lambda x: x.rank)
#         return bestMove.board

#     def isLeaf(self, node):
#         return len(node.children) == 0

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


def miniMax(board):

    if board.currentPlayer == 'X':
        optimal = {'score': -inf, 'i': 0}
    else:
        optimal = {'score': +inf, 'i': 0}

    if board.depth() == 0:
        if board.currentPlayer == 'X' and board.won():
            score = 1
        elif board.currentPlayer == 'O' and board.won():
            score = -1
        else:
            score = 0
        return {'score': score, 'i': 0}
    
    for i in board.empty_spaces():
        board.flatBoard[i] = board.currentPlayer
        board.turn()
        rank = miniMax(board)
        board.flatBoard[i] = ' '
        board.turn()
        rank['i'] = i

        if board.currentPlayer == 'X':
            if rank['score'] > optimal['score']:
                optimal = rank
        else:
            if rank['score'] < optimal['score']:
                optimal = rank
    
    return optimal

            
        