import tkinter as tk
from datetime import datetime
from Field import Field

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    Menu(root, True)
    
def clearChildren(parent):
    for widget in parent.winfo_children():
        widget.destroy()

class Menu:

    def __init__(self, root: tk.Tk, firstCall = False):
        self.root = root
        clearChildren(self.root)
        self.difficulty = tk.StringVar()
        self.difficulty.set("Easy 8x8")
        
        difficulties = ["Easy 8x8", "Medium 16x16", "Hard 30x16", "Custom"]
        difficultyButtons = []
        for i, difficulty in enumerate(difficulties):
            button = tk.Radiobutton(self.root, text=difficulty, variable=self.difficulty, value=difficulty)
            button.grid(row=i, column=0, sticky=tk.W)
            difficultyButtons.append(button)
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=len(difficulties), column=0, sticky=tk.W)
        self.difficulty.trace_add("write",self.showCustom)
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
        self.x.trace_add("write", self.genValidate(self.x, self.xValue, 1, 30))
        self.y.trace_add("write", self.genValidate(self.y, self.yValue, 1, 30))
        self.mines.trace_add("write", self.genValidate(self.mines, self.minesValue, 1, 800))
        
        startGame = tk.Button(self.root, text="Start Game", command=self.startGame)
        startGame.grid(row=len(difficulties)+1, column=0, sticky=tk.W)
        
        #todo: HighScore button

        if firstCall:
            self.root.mainloop()
            
    def genValidate(self,var, val, min, max):
        def validate(_var, _index, _mode):
            try:
                newVal = int(var.get())
                if min <= newVal <= max:
                    val.set(newVal)
            except:
                return
        return validate
        
    
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
            
        
        
    def startGame(self):
        dict = {
            "Easy 8x8": (8, 8, 10),
            "Medium 16x16": (16, 16, 40),
            "Hard 30x16": (30, 16, 99),
            "Custom": (self.xValue.get(), self.yValue.get(), self.minesValue.get())
        }
        x, y, mines = dict[self.difficulty.get()]
        
        if mines < x*y:
            Game(x, y, mines, self.root)

class Game:
    def genLMBClicked(self, x:int, y: int):
        def LMBClicked(event):
            self.field.reveal(x, y)
            self.reloadFieldGUI()
            if self.field.field[x][y].isMine:
                self.buttons[x][y].config(image=self.explodedBomb)
        return LMBClicked

    def genRMBClicked(self,x:int, y: int):
        def RMBClicked(event):
            self.field.flag(x, y)
            self.reloadButton(x, y)
            self.minesLeft.config(text=str(self.field.minesLeft)+" ")

        return RMBClicked

    def disableButton(self, button: tk.Button):
        button.unbind("<Button-1>")
        button.unbind("<Button-3>")
        button["relief"]=tk.SUNKEN

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

    def reloadFieldGUI(self):
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

    # restartbutton
    def restart(self):
        self.running = True
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
        
    def __init__(self, x: int, y: int, mines: int, root: tk.Tk):
        self.root = root
        clearChildren(self.root)
        self.buttons: list[list[tk.Button]] = []
        self.counter = 0
        self.running = True

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