import os
import tkinter as tk
from datetime import datetime
from Field import Field

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    Menu(root, True)

# clear all children of a widget (used to clear the root mainly)  
def clearChildren(parent):
    for widget in parent.winfo_children():
        widget.destroy()
        
# Highscores.txt is formatted as 20 lines, first 5 are easy, next 5 are medium, next 5 are hard, last 5 are custom
# 0 means no highscore
def loadHighscores() -> dict:
    if os.path.exists("highscores.txt"):
        with open("highscores.txt", "r") as file:
            lines = file.readlines()
            highscores = {"Easy 8x8": [], "Medium 16x16": [], "Hard 30x16": [], "Custom": []}
            for i, line in enumerate(lines):
                highscores[list(highscores.keys())[i//5]].append(int(line))
            return highscores
    else:
        return {
            "Easy 8x8": [0,0,0,0,0], 
            "Medium 16x16": [0,0,0,0,0], 
            "Hard 30x16": [0,0,0,0,0], 
            "Custom": [0,0,0,0,0]
                }

# expects highscores as dict with 4 keys and each key has a list of 5 integers
def saveHighscores(highscores: dict):
    with open("highscores.txt", "w") as file:
        for difficulty in highscores:
            for score in highscores[difficulty]:
                file.write(str(score)+"\n")


class Menu:
    # initialize GUI and load highscores
    def __init__(self, root: tk.Tk, firstCall = False):
        self.root = root
        clearChildren(self.root)
        self.difficulty = tk.StringVar()
        self.difficulty.set("Easy 8x8")
        
        difficulties = ["Easy 8x8", "Medium 16x16", "Hard 30x16", "Custom"]
        difficultyButtons = []
        
        # Difficulty Buttons
        difficulty_header = tk.Label(self.root, text="Choose Difficulty", anchor=tk.W)
        difficulty_header.grid(row=0, column=0, sticky=tk.W)
        for i, difficulty in enumerate(difficulties):
            button = tk.Radiobutton(self.root, text=difficulty, variable=self.difficulty, value=difficulty)
            button.grid(row=i+1, column=0, sticky=tk.W)
            difficultyButtons.append(button)
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=len(difficulties)+1, column=0, sticky=tk.W)
        self.difficulty.trace_add("write",self.showCustom)
        
        # custom difficulty variables:
        # x, y, mines are the user inputs
        # xValue, yValue, minesValue are the last valid values inputted
        self.x = tk.StringVar()
        self.x.set(16)
        self.xValue = tk.IntVar()
        self.xValue.set(16)
        self.y = tk.StringVar()
        self.y.set(16)
        self.yValue = tk.IntVar()
        self.yValue.set(16)
        self.mines = tk.StringVar()
        self.mines.set(40)
        self.minesValue = tk.IntVar()
        self.minesValue.set(40)
        
        # validate user input
        self.x.trace_add("write", self.genValidate(self.x, self.xValue, 1, 30))
        self.y.trace_add("write", self.genValidate(self.y, self.yValue, 1, 30))
        self.mines.trace_add("write", self.genValidate(self.mines, self.minesValue, 1, 800))
        
        # load HighScores
        highscore_header = tk.Label(self.root, text="Highscores", anchor=tk.W)
        highscore_header.grid(row=0, column=1, sticky=tk.W)
        highscores = loadHighscores()
        for i, difficulty in enumerate(difficulties):
            highscore_difficulty = highscores[difficulty]
            # format highscores as MM:SS, "--:--" if no highscore
            highscore_string = "\n".join([datetime.fromtimestamp(score).strftime("%M:%S") if score != 0 else "--:--" for score in highscore_difficulty])
            difficulty_header = tk.Label(self.root, text=highscore_string)
            difficulty_header.grid(row=i+1, column=1)
        
        startGame = tk.Button(self.root, text="Start Game", command=self.startGame)
        startGame.grid(row=len(difficulties)+2, column=0,columnspan=2, sticky="ENWS")
        
        # start GUI (must only be called once)
        if firstCall:
            self.root.mainloop()
    
            
    def genValidate(self,var, val, min, max):
        # set value if in bounds
        def validate(_var, _index, _mode):
            try:
                newVal = int(var.get())
                if min <= newVal <= max:
                    val.set(newVal)
            except:
                return
        return validate
        
    # if custom is selected, reveal fields to choose number of fields and mines
    # if it is unselected, clear the fields
    def showCustom(self, _var, _index, _mode):
        if self.difficulty.get() == "Custom":
            x = tk.Entry(self.frame, textvariable=self.x, width=5)
            y = tk.Entry(self.frame, textvariable=self.y, width=5)
            mines = tk.Entry(self.frame, textvariable=self.mines, width=5)
            x.grid(row=0, column=0)
            y.grid(row=0, column=1)
            mines.grid(row=0, column=2)
            xLabel = tk.Label(self.frame, text="x")
            yLabel = tk.Label(self.frame, text="y")
            minesLabel = tk.Label(self.frame, text="mines")
            xLabel.grid(row=1, column=0)
            yLabel.grid(row=1, column=1)
            minesLabel.grid(row=1, column=2)
        else:
            clearChildren(self.frame)
            
    # start the game with the selected difficulty
    def startGame(self):
        dict = {
            "Easy 8x8": (8, 8, 10),
            "Medium 16x16": (16, 16, 40),
            "Hard 30x16": (30, 16, 99),
            "Custom": (self.xValue.get(), self.yValue.get(), self.minesValue.get())
        }
        x, y, mines = dict[self.difficulty.get()]
        
        # check that the game is technically winable (otherwise the generation algorithm might get stuck)
        if mines < x*y:
            Game(x, y, mines, self.root,self.difficulty.get())

class Game:
    def genLMBClicked(self, x:int, y: int):
        
        # reveal all fields recursively
        def LMBClicked(event):
            if self.field.firstGuess:
                self.running = True # start timer
            self.field.reveal(x, y)
            self.reloadFieldGUI()
            if self.field.field[x][y].isMine:
                self.buttons[x][y].config(image=self.explodedBomb)
            self.checkAIMovePossible()
        return LMBClicked

    def genRMBClicked(self,x:int, y: int):
        
        # flag or question a field
        def RMBClicked(event):
            self.field.flag(x, y)
            self.reloadButton(x, y)
            self.minesLeft.config(text=str(self.field.minesLeft)+" ")
            self.checkAIMovePossible()
        return RMBClicked

    def disableButton(self, button: tk.Button):
        button.unbind("<Button-1>")
        button.unbind("<Button-3>")
        button["relief"]=tk.SUNKEN

    # reload a single button
    def reloadButton(self,x,y):
        cell = self.field.field[x][y]
        button: tk.Button = self.buttons[x][y]
        if self.field.disabled:
            self.disableButton(button)
            self.running = False
        if cell.isRevealed:
            if cell.isMine:
                button.config(image=self.bomb, bg="white")
            else:
                button.config(image=self.numbers[cell.neighbours], bg="white")
            self.disableButton(button)
        elif cell.isFlagged:
            button.config(image=self.flag)
        elif cell.isQuestioned:
            button.config(image=self.question)
        else:
            button.config(image=self.hidden)
    
    # reload all buttons
    def reloadFieldGUI(self):
        if self.field.win:
            self.saveHighscore()
        for x in range(self.field.x):
            for y in range(self.field.y):
                self.reloadButton(x, y)
    
    # timer
    def count(self):
        if self.running:
            self.counter += 1
            time = datetime.fromtimestamp(self.counter).strftime("%M:%S")
            self.timer.config(text=time)
        self.timer.after(1000, self.count)
        
    def saveHighscore(self):
        highscores = loadHighscores()
        highscores[self.difficulty] = [score for score in highscores[self.difficulty] if score != 0]
        highscores[self.difficulty].append(self.counter)
        highscores[self.difficulty].sort()
        highscores[self.difficulty] = highscores[self.difficulty][:5]
        highscores[self.difficulty] = highscores[self.difficulty] + [0]*(5-len(highscores[self.difficulty]))
        saveHighscores(highscores)

    # restartbutton
    def restart(self):
        self.running = False
        self.field.__init__(self.field.x, self.field.y, self.field.mines)
        self.reloadFieldGUI()
        self.counter = 0
        self.timer.config(text="00:00")
        for x in range(self.field.x):
            for y in range(self.field.y):
                self.buttons[x][y].config(image=self.hidden, relief=tk.RAISED, bg="lightgrey")
                self.buttons[x][y].bind("<Button-1>", self.genLMBClicked(x, y))
                self.buttons[x][y].bind("<Button-3>", self.genRMBClicked(x, y))

    def menu(self):
        self.running = False
        Menu(self.root)
        
    def notInBounds(self, x, y, i, j):
        return i == 0 and j == 0 or x+i < 0 or x+i >= self.field.x or y+j < 0 or y+j >= self.field.y
    
    # check if next AI move is possible and enable / disable the button depending on it
    def checkAIMovePossible(self, state: bool | None = None):
        btn = self.askAIButton
        if self.field.disabled:
            movePossible = False
        elif state is not None:
            movePossible = state
        else:
            movePossible = self.askAI(True)
        if movePossible:
            btn["state"] = tk.NORMAL
            btn['text'] = "Ask AI"
        else:
            btn["state"] = tk.DISABLED
            btn['text'] = "No AI move available"
    
    # ask a (primitive) AI for the next move
    # will just look whether there are trivial solutions
    # a field with x unmarked neighbours and x mines remaining: all neighbours are mines and will be flagged
    # a field with x marked neighbours and x mines remaining: all other neighbours are safe and will be revealed
    def askAI(self, preview = False):
        for x in range(self.field.x):
            for y in range(self.field.y):
                if self.field.field[x][y].isRevealed and self.field.field[x][y].neighbours > 0:
                    hiddenFields = 0
                    flaggedFields = 0
                    
                    # check all adjacent fields
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if self.notInBounds(x, y, i, j):
                                continue
                            if not self.field.field[x+i][y+j].isRevealed and not self.field.field[x+i][y+j].isFlagged:
                                hiddenFields += 1
                            if self.field.field[x+i][y+j].isFlagged:
                                flaggedFields += 1
                                
                    # if all hidden fields are mines, flag them
                    if hiddenFields == self.field.field[x][y].neighbours - flaggedFields and hiddenFields > 0:
                        if preview:
                            return True
                        for i in range(-1,2):
                            for j in range(-1,2):
                                if self.notInBounds(x, y, i, j):
                                    continue
                                if not self.field.field[x+i][y+j].isRevealed and not self.field.field[x+i][y+j].isFlagged:
                                    # have to call method twice on questioned fields
                                    if self.field.field[x+i][y+j].isQuestioned:
                                        self.field.flag(x+i, y+j)
                                    self.field.flag(x+i, y+j)
                                    self.reloadButton(x+i, y+j)
                        self.checkAIMovePossible()
                        return True
                    
                    # if all mines are flagged, reveal all other fields
                    if flaggedFields == self.field.field[x][y].neighbours and hiddenFields > 0:
                        if preview:
                            return True
                        for i in range(-1,2):
                            for j in range(-1,2):
                                if self.notInBounds(x, y, i, j):
                                    continue
                                if not self.field.field[x+i][y+j].isRevealed and not self.field.field[x+i][y+j].isFlagged:
                                    self.field.reveal(x+i, y+j)
                                    self.reloadFieldGUI()
                        self.checkAIMovePossible()
                        return True
        self.checkAIMovePossible(False)
        return False
        
    # initialize GUI and field
    def __init__(self, x: int, y: int, mines: int, root: tk.Tk, difficulty: str):
        self.difficulty = difficulty
        self.root = root
        clearChildren(self.root)
        self.buttons: list[list[tk.Button]] = []
        self.counter = 0
        self.running = False

        # images
        self.numbers = [tk.PhotoImage(file=f"images/{i}.png") for i in range(9)]
        self.bomb = tk.PhotoImage(file="images/bomb.png")
        self.fakeBomb = tk.PhotoImage(file="images/fakeBomb.png")
        self.explodedBomb = tk.PhotoImage(file="images/explodedBomb.png")
        self.flag = tk.PhotoImage(file="images/flag.png")
        self.hidden = tk.PhotoImage(file="images/hidden.png")
        self.question = tk.PhotoImage(file="images/question.png")
        
        
        self.field = Field(x, y, mines)
        self.timestamp = datetime.fromtimestamp(self.counter)
        self.time = self.timestamp.strftime("%M:%S")
        self.timer = tk.Label(self.root, text=self.time)
        self.timer.grid(row=0, column=0, columnspan=2)
        self.count()

        restartButton = tk.Button(root, text="Restart", command=self.restart)
        restartButton.grid(row=self.field.y+1, column=0, columnspan=self.field.x, sticky="WENS")

        menuButton = tk.Button(root, text="Menu", command=self.menu)
        menuButton.grid(row=self.field.y+2, column=0, columnspan=self.field.x, sticky="WENS")
        
        self.askAIButton = tk.Button(root, text="Ask AI", command=self.askAI)
        self.askAIButton.grid(row=self.field.y+3, column=0, columnspan=self.field.x, sticky="WENS")
        self.checkAIMovePossible(False)

        # mines left
        self.minesLeft = tk.Label(self.root, text=str(self.field.minesLeft)+" ")
        self.minesLeft.grid(row=0, column=self.field.x-2, columnspan=2, sticky=tk.E)

        # grid
        for x in range(self.field.x):
            self.buttons.append([])
            for y in range(self.field.y):
                button = tk.Label(self.root, image=self.hidden, bg="lightgrey", width=20, height=20)
                button.grid(row=y+1, column=x)
                button.bind("<Button-1>", self.genLMBClicked(x, y))
                button.bind("<Button-3>", self.genRMBClicked(x, y))
                self.buttons[x].append(button)

if __name__ == "__main__":
    main()