import numpy as np

k = 9
n = k**2
i = 0
data = np.zeros(shape=(k,k))  # Create a k x k matrix of zeros
while (n>=1):
    # top: right to left
    for l in range(k-i-1,i-1,-1):
        data[i][l] = n
        n -= 1
    # left: top to bottom
    for l in range(i+1,k-i,1):
        data[l][i] = n
        n -= 1
    # bottom: left to right
    for l in range(i+1,k-i,1):
        data[k-i-1][l] = n
        n -= 1
    # right: bottom to top
    for l in range(k-i-2,i,-1):
        data[l][k-i-1] = n
        n -= 1
    i += 1

def addLeadingSpace(n: int, spaces: int) -> str:
    return " " * (spaces - len(str(n))) + str(n)

for i in range(k):
    for j in range(k):
        print(addLeadingSpace(int(data[i][j]),3), end=" ")
    print()