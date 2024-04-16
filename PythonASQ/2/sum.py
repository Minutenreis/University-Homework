x = input("Bitte geben Sie eine Zahl zwischen 0 und 100 ein: ")
y = input("Bitte geben Sie eine weitere Zahl zwischen 0 und 100 ein: ")
x = int(x)
y = int(y)

if x < 0 or x > 100 or y < 0 or y > 100:
    exit("Die Zahlen müssen zwischen 0 und 100 liegen.")

summe = x + y
print("Die Summe der beiden Zahlen beträgt:", summe)