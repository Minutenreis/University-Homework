import random
import sys, os


speicherpfad = os.path.dirname(__file__)

personen = ('Ada', 'Bernd', 'Carina', 'Daniel')
messgeräte = ('Laser', 'Radiometer', 'Thermometer')
monate = ('Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez')

def generiere_Zeile(monat):
    person = random.choice(personen)

    if person == 'Ada':
        return f'{random.choice(messgeräte)},{random.random() * 100},{person},{monat}\n'
    elif person == 'Bernd':
        return f'{random.choice(messgeräte)},{random.random() * 50},{person},{monat}\n'
    elif person == 'Carina':
        return f'{random.choice(messgeräte)},{random.randint(0, 35)},{person},{monat}\n'
    elif person == 'Daniel':
        return f'{random.choice(messgeräte)},{random.random() * random.randint(0, 50)},{person},{monat}\n'

def generiere_Datei(nummer):
    with open(f'{speicherpfad}/Experiment_{nummer+1}.csv', 'w') as ausgabe:
        ausgabe.write('Messgerät,Messwert,Person,Monat\n')
        for monat in monate:
            for i in range(random.randint(50, 150)):
                ausgabe.write(generiere_Zeile(monat))

for i in range(100):
    generiere_Datei(i)