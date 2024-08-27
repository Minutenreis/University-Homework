import random

class Field:
    # Cell class to represent each cell in the field
    class Cell:
        def __init__(self):
            self.isMine = False
            self.isRevealed = False
            self.isFlagged = False
            self.isQuestioned = False
            self.neighbours = 0
    
    # generate field and set defaults
    def __init__(self, x: int, y: int, mines: int):
        self.generateField(x, y, mines)
        self.x = x
        self.y = y
        self.mines = mines
        self.minesLeft = mines
        self.firstGuess = True
        self.revealed = 0
        self.disabled = False
        self.win = False
    
    # generate field, optionally exclude a single position (first click)
    def generateField(self, x: int, y: int, mines: int, x_forbid: int | None = None, y_forbid: int | None = None):
        # 2D array of cells
        self.field = [[self.Cell() for _ in range(y)] for _ in range(x)]
        # all possible spots (excluding the forbidden spot if set)
        allSpots = range(x * y) if (x_forbid is None and y_forbid is None) else range(x * y - 1)
        # mine positions
        mines = random.sample(allSpots, mines)
        # shift mine positions if forbidden spot is set
        if x_forbid is not None and y_forbid is not None:
            mines = [mine + 1 if mine >= x_forbid * y_forbid else mine for mine in mines]
        # apply mines to field, increment all neighbours of mines "neighbours" attribute
        for mine in mines:
            xCoord = mine % x
            yCoord = mine // x
            self.field[xCoord][yCoord].isMine = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= xCoord + i < x and 0 <= yCoord + j < y:
                        self.field[xCoord + i][yCoord + j].neighbours += 1

    # reveal all mines (after game end)
    def __revealAllMines(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.field[i][j].isMine:
                    self.field[i][j].isRevealed = True
                 
    def loseGame(self):
        self.__revealAllMines()
        self.disabled = True
    
    def winGame(self):
        self.__revealAllMines()
        self.disabled = True
        self.win = True
    
    def newGame(self):
        self.__init__(self.x, self.y, self.mines)
    
    # flag cell ("right click"), unflagged -> flagged -> questioned -> unflagged
    # adjust minesLeft accordingly
    def flag(self, x, y):
        if self.field[x][y].isRevealed:
            return
        if not self.field[x][y].isFlagged and not self.field[x][y].isQuestioned:
            # can't flag more mines than there are
            if self.minesLeft == 0:
                return
            self.field[x][y].isFlagged = True
            self.minesLeft -= 1
        elif self.field[x][y].isFlagged:
            self.field[x][y].isFlagged = False
            self.field[x][y].isQuestioned = True
            self.minesLeft += 1
        else:
            self.field[x][y].isQuestioned = False
        
    # reveal cell ("left click")
    # if cell is already revealed or is protected, do nothing
    # if first guess, generate field if mine is hit
    # if cell is mine, lose game
    # force: if a cell is revealed, reveal all neighbours with 0 neighbours regardless of their state
    def reveal(self, x, y, force: bool = False):
        # flagged or protected
        if (self.field[x][y].isFlagged or self.field[x][y].isQuestioned) and not force:
            return
        if self.field[x][y].isRevealed:
            return
        
        # first guess
        if self.firstGuess:
            if self.field[x][y].isMine:
                self.generateField(len(self.field), len(self.field[0]), self.mines, x, y)
            self.firstGuess = False
        
        # reveal field
        self.field[x][y].isRevealed = True
        self.revealed += 1
        
        # lose game if mine is hit
        if self.field[x][y].isMine:
            self.loseGame()
            return
        
        # reveal neighbours if cell has no neighbours
        if self.field[x][y].neighbours == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < len(self.field) and 0 <= y + j < len(self.field[0]):
                        self.reveal(x + i, y + j, True)
        
        # win game if all non-mine cells are revealed
        if self.revealed == len(self.field) * len(self.field[0]) - self.mines:
            self.winGame()
            return