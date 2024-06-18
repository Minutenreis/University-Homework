import randList
import timeit
import profile

def insertionSort(list: list):
    for sorted in range(1, len(list)):
        # find the right place for list[sorted]
        for ind in range(0, sorted):
            if list[sorted] < list[ind]:
                list.insert(ind, list.pop(sorted))
                break
    return list
            

def binaryInsertionSort(list: list):
    for sorted in range(1, len(list)):
        # find the right place for list[sorted]
        left, right = 0, sorted
        while left < right:
            mid = (left + right) // 2
            if list[sorted] < list[mid]:
                right = mid
            else:
                left = mid + 1
        # move list[sorted] to the right place
        list.insert(left, list.pop(sorted))
    return list

def selectionSort(list: list):
    length = len(list)
    for sorted in range(length):
        # find smallest element in unsorted part
        minIndex = sorted
        for i in range(sorted, length):
            if list[i] < list[minIndex]:
                minIndex = i
        # move smallest element to sorted part
        list[sorted], list[minIndex] = list[minIndex], list[sorted]
    return list

# https://en.wikipedia.org/wiki/Merge_sort
def merge(left: list, right: list):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# beides devide and conquer Algorithmen, die in O(n log n) average laufen
# mergeSort ist stabil, quickSort dafür in-place (meist)
def mergeSort(m: list):
    # base case
    if len(m) <= 100:
        return binaryInsertionSort(m)
    
    # devide list into two parts
    left = m[:len(m)//2]
    right = m[len(m)//2:]
    
    # sort both parts
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)


# https://en.wikipedia.org/wiki/Quicksort
def partition(A:list, lo:int, hi:int):
    pivot = A[hi] # more optimal would be median of medians

    # temporary pivot index
    i = lo
    
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    
    # swap pivot with last element
    A[i], A[hi] = A[hi], A[i]
    return i
    
def quickSort(A: list, lo = 0, hi = None):
    if hi is None:
        hi = len(A) - 1
    
    if lo >= hi or lo < 0:
        return A
    
    p = partition(A, lo, hi)
    
    quickSort(A, lo, p-1)
    quickSort(A, p+1, hi)
    
    return A

n = 1000
testList = randList.make_random_list_choices(n)

testListInsertion = testList.copy()
testListInsertionBinary = testList.copy()
testListSelection = testList.copy()
testListMergeSort = testList.copy()
testListQuickSort = testList.copy()

laufzeitInsertion = timeit.timeit(lambda: insertionSort(testListInsertion), globals=globals(), number=1)
laufzeitInsertionBinary = timeit.timeit(lambda: binaryInsertionSort(testListInsertionBinary), globals=globals(), number=1)
laufzeitSelection = timeit.timeit(lambda: selectionSort(testListSelection), globals=globals(), number=1)
laufzeitQuickSort = timeit.timeit(lambda: quickSort(testListQuickSort), globals=globals(), number=1)
laufzeitMergeSort = timeit.timeit(lambda: mergeSort(testListMergeSort), globals=globals(), number=1)
laufzeitPowerSort = timeit.timeit(lambda: testList.sort(), globals=globals(), number=1)

print(f"InsertionSort: {laufzeitInsertion}s")
print(f"BinaryInsertionSort: {laufzeitInsertionBinary}s")
print(f"SelectionSort: {laufzeitSelection}s")
print(f"QuickSort: {laufzeitQuickSort}s")
print(f"MergeSort: {laufzeitMergeSort}s")
print(f"PowerSort: {laufzeitPowerSort}s") # assumes at least Python 3.11

"""
PowerSort << Quicksort < MergeSort << BinaryInsertionSort << InsertionSort < SelectionSort
"""

# profile.run("insertionSort(testListInsertion)", sort="ncalls")
# profile.run("binaryInsertionSort(testListInsertionBinary)", sort="ncalls")
# profile.run("selectionSort(testListSelection)", sort="ncalls")

