import random

# creates a size by size grid with numTrees trees and tents
# 0 is blank, 1 is tree, 2 is tent
def createGrid(size, numTrees):
    grid = [[0]*size for i in range(size)]
    for n in range(numTrees):
        placed = False
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        k = 0
        while not placed:
            if grid[y][x] == 0:
                tentCoor = tentPlace(grid, x, y)
                #tree and assosiated tent can be placed here
                if tentCoor != (-1,-1):
                    grid[y][x] = 1
                    grid[tentCoor[1]][tentCoor[0]] = 2
                    placed = True
            else:
                x = x + 1
                if x == size:    
                    y = (y + 1) % size
                    x = 0
            #no locations are valid tree spots, start again
            if k > size * size:
                return createGrid(size, numTrees)
            k = k + 1
    return grid

"""
def displayGrid(grid):
    vCount = [0] * len(grid)
    for r in grid:
        hCount = 0
        s = " "
        for c in range(len(r)):
            #blank
            if r[c] == 0:
                s = s + "O "
            #tree
            elif r[c] == 1:
                s = s + "T "
            #tent
            elif r[c] == 2:
                s = s + "V "
                hCount = hCount + 1
                vCount[c] = vCount[c] + 1
        s = str(hCount) + s
        print(s)
    s = "  "
    for n in vCount:
        s = s + str(n) + " "
    print(s)
"""

def displayGrid(grid, hCount, vCount):
    s = "  "
    for v in vCount:
        s = s + str(v) + " "
    print(s)
    for r in range(len(grid)):
        s = str(hCount[r]) + " "
        for c in grid[r]:
            #blank
            if c == 0:
                s = s + "O "
            #tree
            elif c == 1:
                s = s + "T "
            #tent
            elif c == 2:
                s = s + "V "
        print(s)
    

def displayPlayerView(playerGrid, hCount, vCount):
    s = "  "
    for v in vCount:
        s = s + str(v) + " "
    print(s)
    for r in range(len(playerGrid)):
        s = str(hCount[r]) + " "
        for c in playerGrid[r]:
            #blank
            if c == 0:
                s = s + "- "
            #tree
            elif c == 1:
                s = s + "T "
            #tent
            elif c == 2:
                s = s + "V "
            elif c == 3:
                s = s + "O "
        print(s)


#returns tuple of coordinates for the tent
#returns -1,-1 if none found
def tentPlace(grid,xTree,yTree):
    n = random.randint(0,4 - 1)
    for i in range(4):
        #n = 0, top
        if (n == 0 and yTree > 0 and grid[yTree - 1][xTree] == 0 and 
            canPlaceTent(grid, xTree, yTree - 1)):
            return (xTree, yTree - 1)
        #n = 1, right
        elif (n == 1 and xTree < len(grid) - 1 and grid[yTree][xTree + 1] == 0 and
              canPlaceTent(grid, xTree + 1, yTree)):
            return (xTree + 1, yTree)
        #n = 2, bottom
        elif (n == 2 and yTree < len(grid) - 1 and grid[yTree + 1][xTree] == 0 and
              canPlaceTent(grid, xTree, yTree + 1)):
            return (xTree, yTree + 1)
        #n = 3, left
        elif (n == 3 and xTree > 0 and grid[yTree][xTree - 1] == 0 and
              canPlaceTent(grid, xTree - 1, yTree)):
            return (xTree - 1, yTree)
    return (-1,-1)
        
#checks to see if any of the surrounding squares are tents
#assumes xTent, yTent are valid locations in grid
def canPlaceTent(grid, xTent, yTent):
    return ((xTent == 0 or grid[yTent][xTent - 1] == 0) and 
            (xTent == len(grid) - 1 or grid[yTent][xTent + 1] == 0) and
            (yTent == 0 or grid[yTent - 1][xTent] == 0) and 
            (yTent == len(grid) - 1 or grid[yTent + 1][xTent] == 0))
    
def isFinished(masterGrid, playerGrid):
    for x in range(len(masterGrid)):
        for y in range(len(masterGrid)):
            if ((masterGrid[x][y] == 2 or playerGrid[x][y] == 2) and 
                masterGrid[x][y] != playerGrid[x][y]):
                return False
    return True
        

def game(size, numTrees):
    #create solved grid
    masterGrid = createGrid(size, numTrees)
    #create the player's grid and 
    playerGrid = [[0]*size for i in range(size)]
    horizontalValues = [0] * size
    verticalValues = [0] * size
    for r in range(size):
        for c in range(size):
            if masterGrid[r][c] == 1:
                playerGrid[r][c] = 1
            if masterGrid[r][c] == 2:
                horizontalValues[r] = horizontalValues[r] + 1
                verticalValues[c] = verticalValues[c] + 1
    solved = False
    while not solved:
        displayPlayerView(playerGrid, horizontalValues, verticalValues)
        playerInput = input("Enter coordinates and value: ")
        if playerInput == "End":
            solved = True
        else:
            xIn, yIn, value = [int(i) for i in playerInput.split()]
            if (xIn < 0 or xIn >= size or yIn < 0 or yIn >= size or
                playerGrid[yIn][xIn] == 1):
                print("Invalid Coordinates")
            elif value == 0:
                playerGrid[yIn][xIn] = 3
            elif value == 2:
                playerGrid[yIn][xIn] = 2
            else:
                print("Invalid Value")
            if isFinished(masterGrid, playerGrid):
                print("Game has been solved!")
                solved = True
    displayGrid(masterGrid, horizontalValues, verticalValues)
    print("End of Game")
        

def main():
    size = 4
    numTrees = 3
    game(size,numTrees)
    

if __name__ == '__main__':
    main()