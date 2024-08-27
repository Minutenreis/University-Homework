
telefonbuch = {}
for i in range(3):
    person = input("Bitte geben Sie zum Speichern einen Kontakt als \"<Name> <Telefonnr.>\" ein: ")
    person = person.split(" ")
    telefonbuch[person[0]] = person[1]

print("Telefonbuch:")
print(telefonbuch)

