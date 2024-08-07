

import random


class Field:
    class Cell:
        def __init__(self, isMine: bool):
            self.isMine = isMine
            self.isRevealed = False
            self.isFlagged = False
            self.isQuestioned = False
            self.neighbours = 0
    
    def __init__(self, x: int, y: int, mines: int):
        if (x == 8 and y == 8 and mines == 10):
            self.mode = "easy"
        elif (x == 16 and y == 16 and mines == 40):
            self.mode = "medium"
        elif (x == 30 and y == 16 and mines == 99):
            self.mode = "hard"
        else:
            self.mode = "custom"
        
        self.generateField(x, y, mines)
        self.resetClock()
        self.x = x
        self.y = y
        self.mines = mines
        self.minesLeft = mines
        self.firstGuess = True
        self.revealed = 0
        self.disabled = False
        
    def generateField(self, x, y, mines):
        self.field = [[self.Cell(False) for _ in range(y)] for _ in range(x)]
        mines = random.sample(range(x * y), mines)
        for mine in mines:
            xCoord = mine % x
            yCoord = mine // x
            self.field[xCoord][yCoord].isMine = True
            self.field[xCoord][yCoord].neighbours = -1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= xCoord + i < x and 0 <= yCoord + j < y:
                        if not self.field[xCoord + i][yCoord + j].isMine:
                            self.field[xCoord + i][yCoord + j].neighbours += 1

    def resetClock(self):
        pass
    
    def stopClock(self):
        pass
    
    def __revealAllMines(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.field[i][j].isMine:
                    self.field[i][j].isRevealed = True
                            
    def loseGame(self):
        self.stopClock()
        self.__revealAllMines()
        self.disabled = True
        # todo: show dialog with "game is lost" "try again" "show Highscores" "exit"
    
    def winGame(self):
        self.stopClock()
        self.__revealAllMines()
        self.disabled = True
        # todo: show dialog with "game is lost" "try again" "show Highscores" "exit"
        # todo: save highscore
    
    def newGame(self):
        self.__init__(self.x, self.y, self.mines)
    
    def flag(self, x, y):
        if self.field[x][y].isRevealed:
            return
        if not self.field[x][y].isFlagged and not self.field[x][y].isQuestioned:
            self.field[x][y].isFlagged = True
            self.minesLeft -= 1
        elif self.field[x][y].isFlagged:
            self.field[x][y].isFlagged = False
            self.field[x][y].isQuestioned = True
            self.minesLeft += 1
        else:
            self.field[x][y].isQuestioned = False
        
    
    def reveal(self, x, y):
        if self.firstGuess:
            while self.field[x][y].isMine:
                # todo: might be slow, need to validate inputs too
                self.generateField(len(self.field), len(self.field[0]), self.minesActual)
                self.firstGuess = False
        if self.field[x][y].isRevealed:
            return
        self.field[x][y].isRevealed = True
        self.revealed += 1
        if self.field[x][y].isMine:
            self.loseGame()
            return
        if self.field[x][y].neighbours == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < len(self.field) and 0 <= y + j < len(self.field[0]):
                        self.reveal(x + i, y + j)
        if self.revealed == len(self.field) * len(self.field[0]) - self.mines:
            self.winGame()
            return
                        
def loadHighscores():
    # check if savefile exists, if not return empty list
    pass

def saveHighscore(time: int, mode: str):
    # load highscores
    # if no highscores exist, create file
    # add highscore to list of mode
    # sort list
    # cut off top 5 again
    # save highscores
    pass              