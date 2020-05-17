import random

class ComputerAI:
    """ A class used to represent the computer player """

    def getMove(self, grid):
        """ 
            Selects an empty cell randomly and places tent
            Restarts if the puzzle isn't solved and the number of placed tents is equal to the number of trees
        """
        cells = grid.getAvailableCells()
        if cells and len(grid.getTents()) < len(grid.getTrees()):
            return ["place",random.choice(cells)]
        else:
            return -1
