from PuzzleGenerator import PuzzleGenerator
from Tree import Tree
from copy import deepcopy


print("test")
gen = PuzzleGenerator(9)
puzzle = gen.getPuzzle()
sol = gen.getSolution()


class HAI:
    def __init__(self, puzzle):
        self.backtrackList = []
        self.placedTents = []
        self.solveRow = deepcopy(puzzle.rowValues)
        self.solveCol = deepcopy(puzzle.colValues)
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
        self.placedTents.append(pos)

    
    def solve(self):
        while len(self.trees) > 0:
            self.backtrackList.append(deepcopy(self))

            self.placeTent(self.trees[0].possibleTentsList[0])
            self.trees.pop(0)
            for tree in self.trees:
                tree.findPossibleTents(self.puzzle, self.solveRow, self.solveCol)
            self.trees.sort(key=lambda x: x.numPossibleTents)

            #backtrack in case of invalid tree
            if len(self.trees) > 0 and self.trees[0].numPossibleTents <= 0:
                self = self.backtrackList.pop(-1)
                #self.backtrackList.pop(-1)
                self.trees[0].possibleTentsList.pop(0)
                self.trees[0].numPossibleTents -= 1
                while self.trees[0].numPossibleTents <= 0: #python has no do while unfortunatly
                    self = self.backtrackList.pop(-1)
                    #self.backtrackList.pop(-1)
                    self.trees[0].possibleTentsList.pop(0)
                    self.trees[0].numPossibleTents -= 1

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
print(out.map)