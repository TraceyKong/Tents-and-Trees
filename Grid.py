from copy import deepcopy

class Grid:
    """ 
        A class used to represent the board of the puzzle 
        
        '-' = empty
        '#' = tent
        'T' = tree
    """

    def __init__(self, size):
        self.size = size                                            # the size of the grid
        self.map = [['-'] * self.size for i in range(self.size)]    # the content of the grid
        self.rowValues = [0] * self.size                            # the list of numbers of tents on each row
        self.colValues = [0] * self.size                            # the list of numbers of tents on each column

    def clone(self):
        """ Returns a copy of the Grid itself """
        gridClone = Grid(self.size)
        gridClone.map = deepcopy(self.map)
        gridClone.rowValues = deepcopy(self.rowValues)
        gridClone.colValues = deepcopy(self.colValues)
        return gridClone

    def checkWithinGrid(self, pos: tuple):
        """ Checks whether the position exists on the grid """
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def setCellValue(self, pos: tuple, val) -> None:
        """ Assigns a new value on position """
        if self.checkWithinGrid(pos):
            self.map[pos[0]][pos[1]] = val

    def getCellValue(self, pos: tuple):
        """ Returns the value at position """
        if self.checkWithinGrid(pos):
            return self.map[pos[0]][pos[1]]
    
    def updateValues(self):
        """ 
            Evaluates the numbers of tents on each row and on each column 
            Then updates rowValues and colValues
        """
        self.rowValues = [0] * self.size
        self.colValues = [0] * self.size
        for row in range(self.size):
            for col in range(self.size):
                if self.map[row][col] == '#':
                    self.rowValues[row] += 1
                    self.colValues[col] += 1

    def displayGrid(self):
        """ Prints the grid """
        print("  ", end="")
        for col in range(len(self.colValues)):
            print("{} ".format(self.colValues[col]), end="")
        print("")
        for row in range(self.size):
            print("{} ".format(self.rowValues[row]), end="")
            for col in range(self.size):
                print("{} ".format(self.map[row][col]), end="")
            print("")
        print("")

    def getAvailableCells(self):
        """ Returns empty cells of the grid """
        return [(row, col)
                for row in range(self.size)
                for col in range(self.size)
                if self.map[row][col] == '-']

    def getCornerCells(self, pos:tuple):
        """ Returns cells that are diagonal to the position """
        if self.checkWithinGrid(pos):
            cells = [(pos[0]-1, pos[1]-1),
                            (pos[0]-1, pos[1]+1),
                            (pos[0]+1, pos[1]-1),
                            (pos[0]+1, pos[1]+1)]

            return [cell for cell in cells if self.checkWithinGrid(cell)]

    def getAdjacentCells(self, pos: tuple):
        """ Returns cells that are adjacent to the position """
        if self.checkWithinGrid(pos):
            cells = [(pos[0]-1, pos[1]),
                            (pos[0], pos[1]-1),
                            (pos[0], pos[1]+1),
                            (pos[0]+1, pos[1])]
        return [cell for cell in cells if self.checkWithinGrid(cell)]

    def getAvailableAdjacentCells(self, pos: tuple):
        """ Returns empty cells that are adjacent to the position """
        if self.checkWithinGrid(pos):
            return [cell for cell in self.getAdjacentCells(pos) if self.map[cell[0]][cell[1]] == '-']

    def getNeighborCells(self, pos: tuple):
        """ Returns cells that are adjacent or diagonal to the position """
        return self.getCornerCells(pos) + self.getAdjacentCells(pos)

    def getAvailableNeighborCells(self, pos: tuple):
        """ Returns the empty cells surrounding the position """
        if self.checkWithinGrid(pos):
            return [cell for cell in self.getNeighborCells(pos) if self.map[cell[0]][cell[1]] == '-']

    def checkValidTentPosition(self, pos: tuple):
        """ 
            Check whether tent can be placed on position.
            Returns True if all surrounding cells are empty, False otherwise
        """
        if self.checkWithinGrid(pos):
            return len(self.getNeighborCells(pos)) == len(self.getAvailableNeighborCells(pos))

    def getTents(self):
        """ Returns the list of cells that contain tents """
        return [(row, col)
                for row in range(self.size)
                for col in range(self.size)
                if self.map[row][col] == '#']

    def getTrees(self):
        """ Returns the list of cells that contain trees """
        return [(row, col)
                for row in range(self.size)
                for col in range(self.size)
                if self.map[row][col] == 'T']
