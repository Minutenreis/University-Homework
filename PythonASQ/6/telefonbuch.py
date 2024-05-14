import json
import os

if not os.path.exists("Telefonbuch.json"):
    with open("Telefonbuch.json", "w") as f:
        f.write("[]")
telefonbuchFile = open("Telefonbuch.json", "r")
# <Name, Nummer>[]
telefonbuch: list[tuple[str,str]] = json.load(telefonbuchFile)


try:
    while True:
        print("1 - Search for number")
        print("2 - Add number")
        print("3 - Get all numbers")
        print("4 - Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            for entry in telefonbuch:
                if entry[0] == name:
                    print(entry[1])
                    break
            else:
                print("Name not found")
        elif choice == "2":
            name = input("Enter name: ")
            number = input("Enter number: ")
            telefonbuch.append((name, number))
        elif choice == "3":
            for entry in telefonbuch:
                print(f"{entry[0]}: {entry[1]}")
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")
except SystemExit:
    json.dump(telefonbuch, open("Telefonbuch.json", "w"))