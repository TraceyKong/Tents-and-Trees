import random, math
from Grid import Grid

class PuzzleGenerator:

    def __init__(self, size):
        self.size = size
        self.grid = Grid(self.size)
        self.difficulty = math.floor(self.size ** 2 * 0.2)
        self.placeTents()
        self.placeTrees()
        self.grid.updateValues()

    def getPuzzle(self):
        gridClone = self.grid.clone()
        for row in range(self.size):
            for col in range(self.size):
                if gridClone.getCellValue((row, col)) == '#':
                    gridClone.setCellValue((row, col), '-')
        return gridClone

    def getSolution(self):
        return self.grid.clone()

    def placeTents(self):
        for i in range(self.difficulty):
            available_cells = self.grid.getAvailableCells()
            new_cell = random.choice(available_cells)
            while not self.grid.checkValidTentPosition(new_cell):
                new_cell = random.choice(available_cells)
            self.grid.setCellValue(new_cell, '#')
    
    def placeTrees(self):
        tents = self.grid.getTents()
        for cell in tents:
            cells = self.grid.getAdjacentCells(cell)
            new_cell = random.choice(cells)
            while self.grid.getCellValue(new_cell) != '-':
                new_cell = random.choice(cells)
            self.grid.setCellValue(new_cell, 'T')

    