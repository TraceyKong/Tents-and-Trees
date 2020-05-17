import re

class Player:
    """ A class used to represent the human player """
    
    def getMove(self, grid):
        """ Evaluates the user input to determine and return the next move """
        cells = grid.getAvailableCells()

        while True:
            moveInput = input("Enter your move: ")
            
            if re.match(r"place \d,\d", moveInput) or re.match(r"erase \d,\d", moveInput):
                move = moveInput.split()
                action = move[0]
                pos = move[1].split(',')

                if (action == "place" and (int(pos[0]), int(pos[1])) in cells) or (action == "erase" and grid.getCellValue((int(pos[0]), int(pos[1]))) != 'T'):
                    return [move[0], (int(pos[0]), int(pos[1]))]
            
            elif moveInput == "restart":
                return -1
            
            elif moveInput == "show solution":
                return 0
            
            print("Move not valid")
