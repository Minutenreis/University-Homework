import time
import random

def min(*numbers: tuple[float]) -> float:
    """Returns the smallest of the given numbers."""
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

def medianControl(*numbers: tuple[float]) -> float:
    """Returns the median of the given numbers."""
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

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

def quickSelct(numbers: list[float], left: int, right: int, k:int) -> float:
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
 
def median(*numbers: tuple[float]) -> float:
    """Returns the median of the given numbers."""
    numbers = list(numbers)
    if(len(numbers) % 2 == 0):
        return (quickSelct(numbers, 0, len(numbers) - 1, len(numbers) // 2 - 1) + quickSelct(numbers, 0, len(numbers) - 1, len(numbers) // 2)) / 2
    else:
        return quickSelct(numbers, 0, len(numbers) - 1, len(numbers) // 2)

def range(start:int, stop:int = None, step:int = 1) -> list[int]:
    """Returns a list of numbers from start to stop with the given step."""
    if step == 0:
        raise ValueError("Step must not be zero")
    if stop == None:
        stop = start
        start = 0
    if start > stop and step > 0:
        return []
    if start < stop and step < 0:
        return []
    numbers = []
    while start < stop and step > 0 or start > stop and step < 0:
        numbers.append(start)
        start += step
    return numbers

x = 1000.0

    