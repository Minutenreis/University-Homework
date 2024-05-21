import random

countLaser = 0
smallestRadio = 1000
biggestNonLaser = 0
laserResults = []

def medianControl(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[len(list) // 2] + list[len(list) // 2 - 1]) / 2
    else:
        return list[len(list) // 2]
    
# https://en.wikipedia.org/wiki/Quickselect
def partition(numbers: list[float], left: int, right: int, pivotIndex: int) -> int:
    pivotValue = numbers[pivotIndex]
    numbers[pivotIndex], numbers[right] = numbers[right], numbers[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if numbers[i] < pivotValue:
            numbers[storeIndex], numbers[i] = numbers[i], numbers[storeIndex]
            storeIndex += 1
    numbers[storeIndex], numbers[right] = numbers[right], numbers[storeIndex]
    return storeIndex

def quickSelect(numbers: list[float], left: int, right: int, k:int) -> float:
    while True:
        if left == right:
            return numbers[left]
        pivotIndex = random.randint(left, right)
        pivotIndex = partition(numbers, left, right, pivotIndex)
        if k == pivotIndex:
            return numbers[k]
        elif k < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1

def median(numbers: list[float]) -> float:
    """Returns the median of the given numbers."""
    if(len(numbers) % 2 == 0):
        return (quickSelect(numbers, 0, len(numbers) - 1, len(numbers) // 2 - 1) + quickSelect(numbers, 0, len(numbers) - 1, len(numbers) // 2)) / 2
    else:
        return quickSelect(numbers, 0, len(numbers) - 1, len(numbers) // 2)



with open("Messwerte.txt", "r") as file:
    messwerte = file.readlines()[1:]
    for messwert in messwerte:
        row = messwert.split(";")
        device = row[0].strip().lower()
        value = float(row[2])
        
        if device == "laser":
            countLaser += 1
            laserResults.append(value)
        else:
            if value > biggestNonLaser:
                biggestNonLaser = value
            if value < smallestRadio and device == "radiometer":
                smallestRadio = value

print(f"Anzahl Laser: {countLaser}")
print(f"Kleinster Radiometerwert: {smallestRadio}")
print(f"Größter Wert ohne Laser: {biggestNonLaser}")
print(f"Durchschnittswert Laser: {sum(laserResults) / len(laserResults)}")
print(f"Median Laser Quickselect: {median(laserResults)}")
print(f"Median Laser Kontrolle: {medianControl(laserResults)}")
            