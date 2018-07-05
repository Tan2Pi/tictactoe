from board import Board

class GameNode:
    def __init__(self, board):
        self.board = board
        self.children = []
    
    def addChild(self, obj):
        self.children.append(obj)

class GameTree:
    depth = 9
    def __init__(self, board):
        self.refreshTree(board)

    def moves(self, node):
        for i in range(Board.size**2):
            if node.board.validMove(i):
                newNode = GameNode(self.board.deepcopy().board.makeMove(i))
                node.addChild(newNode)
    
    # def depthFirst(self, node):
    #     for child in self.root.children:
    #         if child.board == node.board:
    #             return child
    #         else:
    #             self.depthFirst(child.children)

    def refreshTree(self, board):
        self.root = GameNode(board)
        self.moves(self.root)
    

def miniMax(node):
    if node.board.currentPlayer = 'X':
        if node.board.won():
            node.rank = 1
        elif node.board.full():
            node.rank = 0
        else:
            for child in node.children:
                miniMax(child)
    else:
        if node.board.won():
            node.rank = -1
        elif node.board.full():
            node.rank = 0
        else:
            for child in node.children:
                miniMax(child)





    
                

