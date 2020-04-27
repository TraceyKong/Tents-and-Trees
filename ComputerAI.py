import random
from copy import deepcopy

class ComputerAI:
    
    def __init__(self):
        self.validTents = []
        self.rowValues = []
        self.colValues = []
        self.moved = False
    
    def getMove(self, grid):
        if not self.moved:
            self.validTents = self.getValidTents(grid)
            self.rowValues = deepcopy(grid.rowValues)
            self.colValues = deepcopy(grid.colValues)
        self.moved = True
        if len(self.validTents) != 0 and len(grid.getTents()) < len(grid.getTrees()):
            return ["place",self.makeRandomMove()[1]]
        else:
            self.moved = False
            return -1

    def getValidTents(self, grid):
        return [ (t,n) 
                for t in grid.getTrees()
                for n in grid.getAvailableAdjacentCells(t)
                if (grid.rowValues[n[0]] != 0 and
                    grid.colValues[n[1]] != 0) ]
                
    def makeRandomMove(self):
        pos = random.choice(self.validTents)
        self.rowValues[pos[1][0]] = self.rowValues[pos[1][0]] -1
        self.colValues[pos[1][1]] = self.colValues[pos[1][1]] -1
        for tent in self.validTents:
            if (self.rowValues[tent[1][0]] == 0 or self.colValues[tent[1][1]] == 0 or
                tent[0] == pos[0] or
                (abs(tent[1][0]-pos[1][0]) <= 1 and
                abs(tent[1][1]-pos[1][1]) <= 1)):
                self.validTents.remove(tent)
        return pos