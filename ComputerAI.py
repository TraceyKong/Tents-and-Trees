import random

class ComputerAI:
    def getMove(self, grid):
        cells = grid.getAvailableCells()
        if cells and len(grid.getTents()) < len(grid.getTrees()):
            return ["place",random.choice(cells)]
        else:
            return -1
