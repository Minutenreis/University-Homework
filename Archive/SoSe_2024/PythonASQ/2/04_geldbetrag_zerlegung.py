geld = input("Geldbetrag in Euro: ")
geld = int(geld)

fünfhunderter = geld // 500
geld = geld % 500

zweihunderter = geld // 200
geld = geld % 200

hunderter = geld // 100
geld = geld % 100

fuenfziger = geld // 50
geld = geld % 50

zwanziger = geld // 20
geld = geld % 20

zehner = geld // 10
geld = geld % 10

fuenfer = geld // 5
geld = geld % 5

zweier = geld // 2
einer = geld % 2

print("Betrag setzt sich wie folgt zusammen:")
print(fünfhunderter, " mal 500 Euro")
print(zweihunderter, " mal 200 Euro")
print(hunderter, " mal 100 Euro")
print(fuenfziger, " mal 50 Euro")
print(zwanziger, " mal 20 Euro")
print(zehner, " mal 10 Euro")
print(fuenfer, " mal 5 Euro")
print(zweier, " mal 2 Euro")
print(einer, " mal 1 Euro")
