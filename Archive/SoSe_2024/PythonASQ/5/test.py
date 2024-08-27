import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.joinpath('4')))
from mathFunctions import potenz, fakultät
from Uebungsfunktionen import palindrom, verstecken

def test_potenz():
    assert potenz(2, 3) == 8
    assert potenz(2, -3) == 0.125
    assert potenz(2, 0) == 1
    assert potenz(2, 1) == 2
    assert potenz(2, 2) == 4
    assert potenz(2, -2) == 0.25
    assert potenz(2, 4) == 16
    assert potenz(2, -4) == 0.0625
    assert potenz(0,0) == 1
    print("potenz() tests passed")
    
def test_fakultät():
    assert fakultät(0) == 1
    assert fakultät(1) == 1
    assert fakultät(2) == 2
    assert fakultät(3) == 6
    assert fakultät(4) == 24
    assert fakultät(5) == 120
    assert fakultät(6) == 720
    print("fakultät() tests passed")

def test_palindrom():
    assert palindrom("anna") == True
    assert palindrom("Anna") == True
    assert palindrom("Otto") == True
    assert palindrom("Rentner") == True
    assert palindrom("Rentnerin") == False
    assert palindrom("Rentnerinnen") == False
    print("palindrom() tests passed")

def test_verstecken():
    hiddenStr = verstecken("Hallo", 1)
    assert hiddenStr[0] == "H"
    assert hiddenStr[2] == "A"
    assert hiddenStr[4] == "L"
    assert hiddenStr[6] == "L"
    assert hiddenStr[8] == "O"
    print("verstecken() tests passed")

test_fakultät()
test_palindrom()
test_potenz()
test_verstecken()
