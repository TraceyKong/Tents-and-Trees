import random, math
from .Grid import Grid

class PuzzleGenerator:
    """
        A class used to represent a puzzle generator
        
        Generates an playable puzzle of the given size.
    """

    def __init__(self, size):
        self.size = size                                    # the size of the puzzle
        self.grid = Grid(self.size)                         # the grid of the puzzle
        self.difficulty = math.floor(self.size ** 2 * 0.2)  # the number of pairs of tents and trees

        """ Generating the puzzle """
        self.placeTentsAndTrees()                           # places tents and trees on the grid
        self.grid.updateValues()                            # updates the numbers of tents on each row and column

    def getPuzzle(self):
        """
            Returns a copy of the grid without tents
            Erases the tents before returning the grid copy
        """
        gridClone = self.grid.clone()
        for row in range(self.size):
            for col in range(self.size):
                if gridClone.getCellValue((row, col)) == '#':
                    gridClone.setCellValue((row, col), '-')
        return gridClone

    def getSolution(self):
        """ Returns a copy of the grid """
        return self.grid.clone()

    def placeTentsAndTrees(self):
        """ Places tents on the grid randomly """
        for i in range(self.difficulty):
            available_cells = self.grid.getAvailableCells()
            random.shuffle(available_cells)
            placed = False
            for c in available_cells:
                if (self.grid.checkValidTentPosition(c) and 
                    len(self.grid.getAvailableAdjacentCells(c)) > 0):
                    self.grid.setCellValue(c, '#')
                    self.grid.setCellValue(random.choice(self.grid.getAvailableAdjacentCells(c)), 'T')
                    placed = True
                    break
            if not placed:
                self.difficulty = i
                break
