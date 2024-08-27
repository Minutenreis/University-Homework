import random
import time

def skatGen():
    values = ['7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    colours = ['Kreuz','Pik','Herz','Karo']
    for colour in colours:
        for value in values:
            yield colour, value

# shuffles a list of items by swapping randomly chosen cards n times 
def shuffle(list: list, n=100):
    if len(list) < 2:
        return list
    for _ in range(n):
        idx1 = random.randint(0, len(list)-1)
        idx2 = random.randint(0, len(list)-1)
        while idx1 == idx2:
            idx2 = random.randint(0, len(list)-1)
        list[idx1], list[idx2] = list[idx2], list[idx1]

def printSkat(skatDeck: list[tuple[str,str]]):
    valueToShortform = {
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10",
        "Bube": "J",
        "Dame": "Q",
        "König": "K",
        "Ass": "A",
    }
    colourToSymbol = {
        "Kreuz": "♣",
        "Pik": "♠",
        "Herz": "♥",
        "Karo": "♦",
    }
    colourTerminal = {
        "Kreuz": "",
        "Pik": "",
        "Herz": "\033[31m",
        "Karo": "\033[31m",
        "Reset": "\033[0m"
    }
    print("[", end="")
    for i, card in enumerate(skatDeck):
        col, val = card
        print(colourTerminal[col]+colourToSymbol[col]+valueToShortform[val]+colourTerminal["Reset"], end="," if i != len(skatDeck)-1 else "]\n")
    
        
            
iterator = skatGen()

skatDeck = list(skatGen())
printSkat(skatDeck)
start = time.perf_counter()
shuffle(skatDeck,1_000_000)
end = time.perf_counter()
printSkat(skatDeck)
print('time taken for shuffling',end-start, 's')

