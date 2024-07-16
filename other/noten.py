
def calcSchnitt(noten):
    weighted = [el[0]*el[1] for el in noten]
    ectsL = [el[1] for el in noten]
    sumW = sum(weighted)
    ectsSum = sum(ectsL)
    avg = sumW / ectsSum
    return (avg,ectsSum)

# (Note, ECTS)
noten = [
    # B
    (2.3,6), # Lineare Algebra
    (1.7,6), # Grundlagen der Technischen Informatik 
    (2.7,6), # Diskrete Strukturen I 
    (1.3,6), # Grundlagen der Analysis 
    (1.0,6), # Diskrete Strukturen II 
    (1.0,6), # Einführung in die Wahrscheinlichkeitstheorie 
    (1.3,6), # Numerische Mathematik
    # A
    (1.0,9), # Grundlagen informatischer Problemlösung 
    (1.0,5), # Objektorientierte Programmierung 
    (2.0,9), # Algorithmen und Datenstrukturen 
    (1.0,3), # Fortgeschrittenes Programmierpraktikum 
    (2.3,3), # Systemsoftware 
    (1.0,6), # Rechnerstrukturen 
    (1.0,3), # Experimentelle Hardware-Projekte 
    (1.3,9), # Automaten und Berechenbarkeit 
    (1.0,4), # Deklarative Programmierung 
    (1.0,3), # Seminar Software- und Informationssysteme 
    (1.3,6), # Grundlagen der Informations- und Softwaresysteme 
    (1.3,4), # Kryptologie LAB
    (1.0,6), # Kryptologie
    (2.3,6), # Einführung in die Künstliche Intelligenz
    (1.3,6), # Projekt - Paralleles Rechnen 
    (1.0,6), # Parallel Computing I  
    # C
    (1.3,6), # IT-Sicherheit 
    (2.7,6), # Algorithmisches Beweisen
    (1.3,3), # Projektmanagement (ASQ) 
    ]

(avg, ects) = calcSchnitt(noten)
print("Notenschnitt:",avg)
print("ECTS:        ",ects)