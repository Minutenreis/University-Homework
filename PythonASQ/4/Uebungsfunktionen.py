import random


def konkat(*args: tuple[object]) -> str:
    string = ""
    for arg in args:
        string += str(arg)
    return string
        
def palindrom(string: str) -> bool:
    if not isinstance(string, str):
        raise TypeError("Input is not a string")
    string = string.lower()
    for i in range(len(string)//2):
        if string[i] != string[-i-1]:
            return False
    return True

def verstecken(s: str, n = 1) -> str:
    if not isinstance(s, str):
        raise TypeError("s is not a string")
    if not isinstance(n, int):
        raise TypeError("n is not an integer")
    if n < 1:
        raise ValueError("n must be greater than 0")
    s = s.upper()
    string = ""
    for char in s:
        string += char
        for _ in range(n):
            randomChar = chr(random.randint(65,90))
            string += randomChar

    return string

print(verstecken("Hallo", 3))