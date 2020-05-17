from PuzzleGenerator import PuzzleGenerator
from Tree import Tree



gen = PuzzleGenerator(8)
puzzle = gen.getPuzzle()
sol = gen.getSolution()


class HAI:
    def __init__(self, puzzle):
        self.placedTents = []
        self.solveRow = puzzle.rowValues
        self.solveCol = puzzle.colValues
        self.puzzle = puzzle
        initialTreeList = puzzle.getTrees()
        self.trees = []
        for item in initialTreeList:
            self.trees.append(Tree(item, puzzle, self.solveRow, self.solveCol))
        self.trees.sort(key=lambda x: x.numPossibleTents)


    def placeTent(self, pos):
        self.puzzle.map[pos[0]][pos[1]] = '#'
        self.solveRow[pos[0]] -= 1
        self.solveCol[pos[1]] -= 1

    
    def solve(self):
        while not self.isSolved():
            self.placeTent(self.trees[0].possibleTentsList[0])
            self.trees.pop(0)
            for tree in self.trees:
                tree.findPossibleTents(self.puzzle, self.solveRow, self.solveCol)
            self.trees.sort(key=lambda x: x.numPossibleTents)
        return self.puzzle
            


    def isSolved(self):
        """
            Returns True if there are as many tents as trees, False otherwise
        """
        if len(self.placedTents) != len(puzzle.getTrees()):
            return False
        return True

obj = HAI(puzzle)
out = obj.solve()
print("test")