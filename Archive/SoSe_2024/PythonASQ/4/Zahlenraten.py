import random

zufallszahl = random.randint(0,100)

while(True):
    try:
        guess = int(input("Geben Sie eine Zahl zwischen 0 und 100 ein: "))
    except ValueError:
        exit("Es dürfen nur Ziffern eingegeben werden")
    if guess == zufallszahl:
        print("Herzlichen Glückwunsch! Sie haben die Zahl erraten!")
        break
    elif guess < zufallszahl:
        print("Die gesuchte Zahl ist größer.")
    else:
        print("Die gesuchte Zahl ist kleiner.")