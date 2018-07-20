from board import Board
from copy import deepcopy

class GameNode:
    def __init__(self, board):
        self.board = board
        self.children = []
        self.rank = 0
    
    def addChild(self, obj):
        self.children.append(obj)

class GameTree:
    depth = 9
    def __init__(self, board):
        self.refresh(board)

    def moves(self, node):
        for i in range(Board.size**2):
            if node.board.validMove(i):
                newBoard = deepcopy(node.board)
                newBoard.makeMove(i)
                newBoard.turn()
                newNode = GameNode(newBoard)
                node.addChild(newNode)
    
    # def depthFirst(self, node):
    #     for child in self.root.children:
    #         if child.board == node.board:
    #             return child
    #         else:
    #             self.depthFirst(child.children)

    def refresh(self, board):
        self.root = GameNode(board)
        self.moves(self.root)
    
    def bestMove(self):
        miniMax(self.root)
        bestMove = max(self.root.children, key = lambda x: x.rank)
        return bestMove.board
    

def miniMax(node):
    if node.board.currentPlayer == 'X':
        if node.board.won():
            node.rank = 1
        elif node.board.full():
            node.rank = 0
        else:
            for child in node.children:
                node.rank = miniMax(child)
    else:
        if node.board.won():
            node.rank = -1
        elif node.board.full():
            node.rank = 0
        else:
            for child in node.children:
                node.rank = miniMax(child)





    
                

