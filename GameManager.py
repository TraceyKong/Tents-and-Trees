from PuzzleGenerator import PuzzleGenerator
import time

class GameManager:
    """ A class used to represent the game manager """
    
    def __init__(self, player, size=10):
        self.size = size                                        # the size of the puzzle
        self.puzzleGenerator = PuzzleGenerator(size)            # the puzzle generator
        self.puzzle = self.puzzleGenerator.getPuzzle()          # the grid of the puzzle
        self.solution = self.puzzleGenerator.getSolution()      # the grid of the solution
        self.player = player                                    # the player

    def checkSolved(self):
        """ Checks whether the puzzle grid is equal to the solution grid """
        return self.puzzle.map == self.solution.map
    
    def restart(self):
        """ Restores the puzzle grid to the beginning """
        self.puzzle = self.puzzleGenerator.getPuzzle()

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


    