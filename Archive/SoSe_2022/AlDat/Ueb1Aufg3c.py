
from array import array

def checkPermutation(perm: array):
    high = 0
    stack = []
    for i in range(0, len(perm)):
        if perm[i] > high:
            for j in range(high+1, perm[i]):
                stack.append(j)
            high = perm[i]
        else:
            if(perm[i] != stack.pop()):
                return False
    return True

def main():
    print("Hello World!")
    print(checkPermutation([1,2,5,3,4,6]))


if __name__ == "__main__":
    main()



