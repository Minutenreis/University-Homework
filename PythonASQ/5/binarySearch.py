
def binarySearchIteration(list, element):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == element:
            return True
        elif list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return False

def binarySearchTailRecursion(list, element):
    def helper(left, right):
        if left > right:
            return None, False
        mid = (left + right) // 2
        if list[mid] == element:
            return None ,True
        elif list[mid] < element:
            return helper, (mid + 1, right)
        else:
            return helper, (left, mid - 1)
    
    # pythonic tail recursion see http://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html
    func, args = helper, (0, len(list) - 1)
    while func != None:
        func, args = func(*args)
    return args

# once again tail recursion basically does the same thing as the iterative variant, just less well
def binarySearchRecursion(list, element, left = 0, right = None):
    if right == None:
        right = len(list) - 1
    if left > right:
        return False
    mid = (left + right) // 2
    if list[mid] == element:
        return True
    elif list[mid] < element:
        return binarySearchRecursion(list, element, mid + 1, right)
    else:
        return binarySearchRecursion(list, element, left, mid - 1)

# this is only efficient for np.arrays
def binarySearchRecursionSlice(list, element):
    if len(list) == 0:
        return False
    mid = len(list) // 2
    if list[mid] == element:
        return True
    elif list[mid] < element:
        return binarySearchRecursionSlice(list[mid+1:], element)
    else:
        return binarySearchRecursionSlice(list[:mid], element)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("binarySearch")
print("Iteration, Tailrecursion, Recursion, RecursionSlice:")
print(binarySearchIteration(list, 5), binarySearchTailRecursion(list, 5), binarySearchRecursion(list, 5), binarySearchRecursionSlice(list, 5))
print(binarySearchIteration(list, 11), binarySearchTailRecursion(list, 11), binarySearchRecursion(list, 11), binarySearchRecursionSlice(list, 11))