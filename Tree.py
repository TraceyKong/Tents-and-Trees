class Tree:
    def __init__(self, pos, puzzle, curRowValues, curColValues):
        self.pos = pos
        self.numPossibleTents = 0
        self.possibleTentsList = []
        self.findPossibleTents(puzzle, curRowValues, curColValues)

    def findPossibleTents(self, puzzle, curRowValues, curColValues):
        self.possibleTentsList = []
        if puzzle.checkifValidTent((self.pos[0]-1, self.pos[1]), curRowValues, curColValues): #check above
            self.possibleTentsList.append((self.pos[0]-1, self.pos[1]))
            self.numPossibleTents = len(self.possibleTentsList)
        
        if puzzle.checkifValidTent((self.pos[0]+1, self.pos[1]), curRowValues, curColValues): #check below
            self.possibleTentsList.append((self.pos[0]+1, self.pos[1]))
            self.numPossibleTents = len(self.possibleTentsList)
        
        if puzzle.checkifValidTent((self.pos[0], self.pos[1]-1), curRowValues, curColValues): #check left
            self.possibleTentsList.append((self.pos[0], self.pos[1]-1))
            self.numPossibleTents = len(self.possibleTentsList)

        if puzzle.checkifValidTent((self.pos[0], self.pos[1]+1), curRowValues, curColValues): #check right
            self.possibleTentsList.append((self.pos[0], self.pos[1]+1))
            self.numPossibleTents = len(self.possibleTentsList)
