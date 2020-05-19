import random
from copy import deepcopy

class ComputerAI:
    
    """ 
        A class used to represent the human player 
        Finds the correct tents using basic backtracking search
        TODO:
            DFS-backtracking search - done, no optimizations
            Arc-consitency tests
    """
    
    def __init__(self):
        self.validTents = []
        self.rowValues = []
        self.colValues = []
        self.solvedTents = []
        self.turn = 0
    
    def getMove(self, grid):
        """
            Returns the grid location if one exists, otherwise returns -1
        """
        #start of the game, store the values for the grid
        if self.turn == 0:
            self.validTents = self.getValidTents(grid)
            self.rowValues = deepcopy(grid.rowValues)
            self.colValues = deepcopy(grid.colValues)
            tempGrid = grid.clone()
            self.solve(tempGrid)
        self.turn = self.turn + 1
        #return each position of the tents
        return["place", self.solvedTents[self.turn - 1][1]]

        """
        Old Code for random search:
            
        self.turn = self.turn + 1
        #a valid tent exists and there are fewer tents than trees
        if len(self.validTents) != 0 and len(grid.getTents()) < len(grid.getTrees()):
            return ["place",self.makeRandomMove()[1]]
        #no valid tent exists, restart the board
        else:
            self.turn = 0
            return -1
        """
    

    def getValidTents(self, grid):
        """
            Returns list of valid tent/grid pairs:
                [ ( (tree_x1, tree1_y), [(tent1_x,tent1_y), ...]) , ... ]
            Only called to populate the list at the beginning of each game
        """
        tents = []
        for t in grid.getTrees():
            treeAndTent = (t,[])
            for n in grid.getAvailableAdjacentCells(t):
                if (grid.rowValues[n[0]] != 0 and grid.colValues[n[1]] != 0):
                    treeAndTent[1].append(n)
            tents.append(treeAndTent)
        return tents
             
    def solve(self, grid):
        """
            Generates list of correct tent locations
        """
        if self.solved(grid):
            return True
        #sort by minimum remaining values
        self.validTents.sort(key = lambda x: len(x[1]))
        currentTree = self.validTents[0]
        #create copy of previous values for backtracking
        previousValidTents = deepcopy(self.validTents)
        previousRowValues = deepcopy(self.rowValues)
        previousColValues = deepcopy(self.colValues)
        for currentTent in currentTree[1]:
            #place tent in a cell, assume it's correct
            self.updateValidTents( (currentTree[0], currentTent) )
            self.solvedTents.append( (currentTree[0], currentTent) )
            grid.setCellValue(currentTent,'#')
            #test if cell is in a valid spot for a tent
            if not self.invalidState(grid):
                result = self.solve(grid)
                if result:
                    return result
            #cell not valid, backtrack
            self.solvedTents.remove( (currentTree[0], currentTent) )
            grid.setCellValue(currentTent,'-')
            #copy previous values if backtracking
            self.validTents = deepcopy(previousValidTents)
            self.rowValues = deepcopy(previousRowValues)
            self.colValues = deepcopy(previousColValues)
        return False
            
    
    def solved(self,grid):
        """
            Returns True if there are as many tents as trees, False otherwise
        """
        if len(self.solvedTents) != len(grid.getTrees()):
            return False
        return True
        
    def invalidState(self, grid):
        """
            Returns True if the grid is invalid, False otherwise
            Invalid means that there is a tree with no possible locations for a tent
        """
        for tree in self.validTents:
            if len(tree[1]) == 0:
                return True
        return False

    def updateValidTents(self, treeAndTentIn):
        """
            Updates the internal list of row and column values,
            and the list of valid tree-tent pairs
            Input is in the form ((tree_x,tree_y),(tent_x,tent_y))
        """
        #decrement row and column values
        self.rowValues[treeAndTentIn[1][0]] = self.rowValues[treeAndTentIn[1][0]] -1
        self.colValues[treeAndTentIn[1][1]] = self.colValues[treeAndTentIn[1][1]] -1
        for tree in self.validTents:
            #remove tree of input tent
            if treeAndTentIn[0] == tree[0]:
                self.validTents.remove(tree)
                break
        for tree in self.validTents:
            toRemove = []
            for tent in tree[1]:
                #remove tent if its row or column values or 0, 
                #or if it is 1 square away from the current input tent
                if (self.rowValues[tent[0]] == 0 or self.colValues[tent[1]] == 0 or
                (abs(tent[0]-treeAndTentIn[1][0]) <= 1 and
                 abs(tent[1]-treeAndTentIn[1][1]) <= 1)):
                    toRemove.append(tent)
            for tent in toRemove:
                tree[1].remove(tent)
    
    """
    following code is for random move selection, unused in current backtracking algorithm
    """
    
    def selectTent(self):
        """
            Returns a random (tent, tree) tuple from the list of valid moves
        """
        tree = random.choice(self.validTents)
        tent = random.choice(tree[1])
        return (tree[0],tent)
    
    def makeRandomMove(self):
        """
            Returns a random valid location for a tree
            Updates list to remove locations that are no longer valid
                Works as foward checking
        """
        pos = random.choice(self.validTents)
        self.rowValues[pos[1][0]] = self.rowValues[pos[1][0]] -1
        self.colValues[pos[1][1]] = self.colValues[pos[1][1]] -1
        for tent in self.validTents:
            if (self.rowValues[tent[1][0]] == 0 or self.colValues[tent[1][1]] == 0 or
                tent[0] == pos[0] or
                (abs(tent[1][0]-pos[1][0]) <= 1 and
                abs(tent[1][1]-pos[1][1]) <= 1)):
                self.validTents.remove(tent)
        return pos

