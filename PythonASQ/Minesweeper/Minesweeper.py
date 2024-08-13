import tkinter as tk
from datetime import datetime
from Field import Field

def genLMBClicked(x:int, y: int):
    def LMBClicked(event):
        field.reveal(x, y)
        reloadFieldGUI()
        if field.field[x][y].isMine:
            buttons[x][y].config(image=explodedBomb)
    return LMBClicked

def genRMBClicked(x:int, y: int):
    def RMBClicked(event):
        field.flag(x, y)
        reloadButton(x, y)
        minesLeft.config(text=str(field.minesLeft)+" ")
    
    return RMBClicked

def disableButton(button: tk.Button):
    button.unbind("<Button-1>")
    button.unbind("<Button-3>")
    button["relief"]=tk.SUNKEN

def reloadButton(x,y):
    cell = field.field[x][y]
    button: tk.Button = buttons[x][y]
    if field.disabled:
        disableButton(button)
        global running
        running = False
    if cell.isRevealed:
        if cell.isMine:
            button.config(image=bomb, bg="white")
        else:
            button.config(image=numbers[cell.neighbours], bg="white")
        disableButton(button)
    elif cell.isFlagged:
        button.config(image=flag)
    elif cell.isQuestioned:
        button.config(image=question)
    else:
        button.config(image=hidden)

def reloadFieldGUI():
    for x in range(field.x):
        for y in range(field.y):
            reloadButton(x, y)


field = Field(8, 8, 10)
root = tk.Tk()
root.title("Minesweeper")
numbers = [tk.PhotoImage(file=f"images/{i}.png") for i in range(9)]
bomb = tk.PhotoImage(file="images/bomb.png")
fakeBomb = tk.PhotoImage(file="images/fakeBomb.png")
explodedBomb = tk.PhotoImage(file="images/explodedBomb.png")
flag = tk.PhotoImage(file="images/flag.png")
hidden = tk.PhotoImage(file="images/hidden.png")
question = tk.PhotoImage(file="images/question.png")
buttons: list[list[tk.Button]] = []
counter = 0
running = True

# timer
def count():
    global counter
    if running:
        counter += 1
        time = datetime.fromtimestamp(counter).strftime("%M:%S")
        timer.config(text=time)
    timer.after(1000, count)

timestamp = datetime.fromtimestamp(counter)
time = timestamp.strftime("%M:%S")
timer = tk.Label(root, text=time)
timer.grid(row=0, column=0, columnspan=2)
count()

bottomBar = tk.Frame(root)
bottomBar.grid(row=field.x+1, column=0, columnspan=field.y, rowspan=1, sticky=tk.W)
bottomBar.grid_propagate(False)

# restartbutton
def restart():
    global running
    global counter
    running = True
    field.__init__(field.x, field.y, field.mines)
    reloadFieldGUI()
    counter = 0
    timer.config(text="00:00")
    for x in range(field.x):
        for y in range(field.y):
            buttons[x][y].config(image=hidden, relief=tk.RAISED, bg="lightgrey")
            buttons[x][y].bind("<Button-1>", genLMBClicked(x, y))
            buttons[x][y].bind("<Button-3>", genRMBClicked(x, y))

restartButton = tk.Button(bottomBar, text="Restart", command=restart)
restartButton.pack(side=tk.LEFT, fill=tk.X)

# quitbutton todo: show menu
def quit():
    global running
    running = False
    root.quit()

quitButton = tk.Button(bottomBar, text="Quit", command=quit)
quitButton.pack(side=tk.LEFT, fill=tk.X)

# mines left
minesLeft = tk.Label(root, text=str(field.minesLeft)+" ")
minesLeft.grid(row=0, column=field.y-2, columnspan=2, sticky=tk.E)

# grid
for x in range(field.x):
    buttons.append([])
    for y in range(field.y):
        button = tk.Label(root, image=hidden, bg="lightgrey", width=20, height=20)
        button.grid(row=x+1, column=y)
        button.bind("<Button-1>", genLMBClicked(x, y))
        button.bind("<Button-3>", genRMBClicked(x, y))
        buttons[x].append(button)
        


root.mainloop()


