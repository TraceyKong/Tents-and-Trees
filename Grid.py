from copy import deepcopy

class Grid:

    def __init__(self, size):
        self.size = size
        self.map = [['-'] * self.size for i in range(self.size)]
        self.rowValues = [0] * self.size
        self.colValues = [0] * self.size

    def clone(self):
        gridClone = Grid(self.size)
        gridClone.map = deepcopy(self.map)
        gridClone.rowValues = deepcopy(self.rowValues)
        gridClone.colValues = deepcopy(self.colValues)
        return gridClone

    def checkWithinGrid(self, pos: tuple):
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def setCellValue(self, pos: tuple, val) -> None:
        if self.checkWithinGrid(pos):
            self.map[pos[0]][pos[1]] = val

    def getCellValue(self, pos: tuple):
        if self.checkWithinGrid(pos):
            return self.map[pos[0]][pos[1]]
    
    def updateValues(self):
        self.rowValues = [0] * self.size
        self.colValues = [0] * self.size
        for row in range(self.size):
            for col in range(self.size):
                if self.map[row][col] == '#':
                    self.rowValues[row] += 1
                    self.colValues[col] += 1

    def displayGrid(self):
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
        return [(row, col)
                for row in range(self.size)
                for col in range(self.size)
                if self.map[row][col] == '-']

    def getCornerCells(self, pos:tuple):
        if self.checkWithinGrid(pos):
            cells = [(pos[0]-1, pos[1]-1),
                            (pos[0]-1, pos[1]+1),
                            (pos[0]+1, pos[1]-1),
                            (pos[0]+1, pos[1]+1)]

        return [cell for cell in cells if self.checkWithinGrid(cell)]

    def getAdjacentCells(self, pos: tuple):
        if self.checkWithinGrid(pos):
            cells = [(pos[0]-1, pos[1]),
                            (pos[0], pos[1]-1),
                            (pos[0], pos[1]+1),
                            (pos[0]+1, pos[1])]

        return [cell for cell in cells if self.checkWithinGrid(cell)]

    def getAvailableAdjacentCells(self, pos: tuple):
        if self.checkWithinGrid(pos):
            return [cell for cell in self.getAdjacentCells(pos) if self.map[cell[0]][cell[1]] == '-']

    def getNeighborCells(self, pos: tuple):
        return self.getCornerCells(pos) + self.getAdjacentCells(pos)

    def getAvailableNeighborCells(self, pos: tuple):
        if self.checkWithinGrid(pos):
            return [cell for cell in self.getNeighborCells(pos) if self.map[cell[0]][cell[1]] == '-']

    def checkValidTentPosition(self, pos: tuple):
        if self.checkWithinGrid(pos):
            return len(self.getNeighborCells(pos)) == len(self.getAvailableNeighborCells(pos))

    def getTents(self):
        return [(row, col)
                for row in range(self.size)
                for col in range(self.size)
                if self.map[row][col] == '#']

    def getTrees(self):
        return [(row, col)
                for row in range(self.size)
                for col in range(self.size)
                if self.map[row][col] == 'T']
