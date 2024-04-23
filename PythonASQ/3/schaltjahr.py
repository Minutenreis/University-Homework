while True:
    input_year = input("Geben Sie ein Jahr ein: ")
    try :
        year = int(input_year)
    except: 
        print("Programm beendet")
        break
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Schaltjahr")
    else:
        print("Kein Schaltjahr")