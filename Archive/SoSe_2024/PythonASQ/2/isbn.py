isbn = input("Bitte geben Sie die ersten 9 Ziffern einer ISBN-10 ein: ")
isbn = int(isbn)

s = 0
factor = 9
for i in range(1, 10):
    s += isbn % 10 * factor
    isbn = isbn // 10
    factor -= 1
    
pruef = s % 11
if pruef == 10:
    pruef = "X"
    
print("Die Prüfziffer der ISBN-10 ist:", pruef)