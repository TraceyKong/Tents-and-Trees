from ComputerAI import ComputerAI
from Player import Player
from GameManager import GameManager
import sys

if __name__ == "__main__":
    args = sys.argv
    
    if args[1] == "human":
        player = Player()
    elif args[1] == "computer":
        player = ComputerAI()

    puzzle = GameManager(player)
    puzzle.start()

