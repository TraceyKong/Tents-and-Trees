from .PuzzleGenerator import PuzzleGenerator
import time

class GameManager:
    """ A class used to represent the game manager """
    
    def __init__(self, player, size=10):
        self.size = size                                        # the size of the puzzle
        self.puzzleGenerator = PuzzleGenerator(size)            # the puzzle generator
        self.puzzle = self.puzzleGenerator.getPuzzle()          # the grid of the puzzle
        self.solution = self.puzzleGenerator.getSolution()      # the grid of the solution
        self.player = player                                    # the player
        self.solved = False

    def checkSolved(self):
        """ Checks whether the puzzle grid is equal to the solution grid """
        if(self.puzzle.map == self.solution.map):
            return True
        else:
            tents = self.puzzle.getTents()
            for col in range(self.puzzle.size):
                c_tents = [pos for pos in tents if pos[1] == col]
                if len(c_tents) != self.puzzle.colValues[col]:
                    return False
            for row in range(self.puzzle.size):
                r_tents = [pos for pos in tents if pos[0] == row]
                if len(r_tents) != self.puzzle.rowValues[row]:
                    return False
            return True
    
    def restart(self):
        """ Restores the puzzle grid to the beginning """
        self.puzzle = self.puzzleGenerator.getPuzzle()

    def play(self, pos):
        if not self.solved and self.puzzle.checkWithinGrid(pos):
            if self.puzzle.getCellValue(pos) == '-':
                self.puzzle.setCellValue(pos, '#')

            elif self.puzzle.getCellValue(pos) == '#':
                self.puzzle.setCellValue(pos, '-')
            
            if self.checkSolved():
                self.solved = True

    def start(self):
        """ Runs the puzzle """
        turns = 0
        start = time.process_time()

        self.puzzle.displayGrid()

        while not self.checkSolved():
            move = self.player.getMove(self.puzzle)
            turns = turns + 1
            if move != -1 and move != 0 and self.puzzle.checkWithinGrid(move[1]):
                action = move[0]
                pos = move[1]

                # places tent on position
                if action == "place":
                    print("Placed tent on ", pos[0],',',pos[1])
                    self.puzzle.setCellValue(pos, '#')

                # erases tent on position
                elif action == "erase":
                    print("Erased tent at ", pos[0],',',pos[1])
                    self.puzzle.setCellValue(pos, '-')
                
                self.puzzle.displayGrid()

            # restarts the puzzle
            elif move == -1:
                print("Restart")
                self.restart()
            
                self.puzzle.displayGrid()

            # prints the solution and ends the game
            elif move == 0:
                print("Solution:")
                self.solution.displayGrid()
                break
        self.puzzle.displayGrid()
        print("Congrats! You've solved the puzzle in " + str(turns) + " turns and "+
              str(time.process_time() - start) + " seconds.")


  
