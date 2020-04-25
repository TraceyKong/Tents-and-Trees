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

def displayGrid(grid):
    for r in grid:
        s = " "
        for c in r:
            #blank
            if c == 0:
                s = s + "-"
            #tree
            elif c == 1:
                s = s + "T"
            #tent
            elif c == 2:
                s = s + "V"
            s = s + " "
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
    return ((xTent == 0 or grid[yTent][xTent - 1] != 2) and 
            (xTent == len(grid) - 1 or grid[yTent][xTent + 1] != 2) and
            (yTent == 0 or grid[yTent - 1][xTent] != 2) and 
            (yTent == len(grid) - 1 or grid[yTent + 1][xTent] != 2))
        

def main():
    grid = createGrid(8,12)
    displayGrid(grid)

if __name__ == '__main__':
    main()