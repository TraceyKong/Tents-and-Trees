from PuzzleGenerator import PuzzleGenerator

class GameManager:

    def __init__(self, player, size=5):
        self.size = 5
        self.puzzleGenerator = PuzzleGenerator(size)
        self.puzzle = self.puzzleGenerator.getPuzzle()
        self.solution = self.puzzleGenerator.getSolution()
        self.player = player

    def checkSolved(self):
        return self.puzzle.map == self.solution.map
    
    def restart(self):
        self.puzzle = self.puzzleGenerator.getPuzzle()

    def start(self):
        self.puzzle.displayGrid()

        while not self.checkSolved():
            move = self.player.getMove(self.puzzle)

            if move != -1 and move != 0 and self.puzzle.checkWithinGrid(move[1]):
                action = move[0]
                pos = move[1]

                if action == "place":
                    print("Placed tent on ", pos[0],',',pos[1])
                    self.puzzle.setCellValue(pos, '#')

                elif action == "erase":
                    print("Erased tent at ", pos[0],',',pos[1])
                    self.puzzle.setCellValue(pos, '-')
                
                self.puzzle.displayGrid()

            elif move == -1:
                print("Restart")
                self.restart()
            
                self.puzzle.displayGrid()

            elif move == 0:
                print("Solution:")
                self.solution.displayGrid()
                break

        print("Congrats! You've solved the puzzle.")


    