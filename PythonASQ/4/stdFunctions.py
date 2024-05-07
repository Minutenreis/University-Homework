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

def range_control(start:int, stop:int = None, step:int = 1) -> list[int]:
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

class RangeIterator:
    curr = 0;
    stop = 0;
    step = 1;
    
    def __init__(self, start:int, stop:int, step:int):
        """Returns a list of numbers from start to stop with the given step."""
        self.start = start
        self.stop = stop
        self.step = step
    
    def __next__(self):
        if self.curr >= self.stop and self.step > 0 or self.curr <= self.stop and self.step < 0:
            raise StopIteration
        val = self.curr
        self.curr += self.step
        return val

class Range:
    start = 0
    stop = 0
    step = 1
    
    def __init__(self, start:int, stop:int = None, step:int = 1) -> list[int]:
        """Returns a list of numbers from start to stop with the given step."""
        if step == 0:
            raise ValueError("range() arg 3 must not be zero")
        if stop == None:
            self.stop = start
            self.start = 0
        else:
            self.start = start
            self.stop = stop
        self.step = step
    
    def __iter__(self):
        return RangeIterator(self.start, self.stop, self.step)
    
    def __repr__(self):
        return "range(" + str(self.start) + ", " + str(self.stop) + ", " + str(self.step) + ")"
        
def range(start:int, stop:int = None, step:int = 1) -> Range:
    return Range(start, stop, step)