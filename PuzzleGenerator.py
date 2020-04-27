import random, math
from Grid import Grid

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
        self.placeTents()                                   # places tents on the grid
        self.placeTrees()                                   # places trees on the grid
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

    def placeTents(self):
        """ Places tents on the grid randomly """
        for i in range(self.difficulty):
            available_cells = self.grid.getAvailableCells()
            new_cell = random.choice(available_cells)
            while not self.grid.checkValidTentPosition(new_cell):
                new_cell = random.choice(available_cells)
            self.grid.setCellValue(new_cell, '#')
    
    def placeTrees(self):
        """ Places trees next to the tents randomly """
        tents = self.grid.getTents()
        for cell in tents:
            cells = self.grid.getAdjacentCells(cell)
            new_cell = random.choice(cells)
            while self.grid.getCellValue(new_cell) != '-':
                new_cell = random.choice(cells)
            self.grid.setCellValue(new_cell, 'T')

    