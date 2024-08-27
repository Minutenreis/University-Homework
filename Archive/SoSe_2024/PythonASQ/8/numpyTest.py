import numpy as np

arr1Arange = np.arange(1, 21)
arr1Linspace = np.linspace(1, 20, 20)

print(arr1Arange)
print(arr1Linspace)
print()

arr2Arange = np.arange(0, 4.6, 0.3)
arr2Linspace = np.linspace(0, 4.5, 16)

print(arr2Arange)
print(arr2Linspace)
print()

arr3Arange = np.arange(5,10.1,0.625)
arr3Linspace = np.linspace(5, 10, 9)

print(arr3Arange)
print(arr3Linspace)
print()

arr4Arange = np.arange(0, 20.1, 20/7)
arr4Linspace = np.linspace(0, 20, 8)

print(arr4Arange)
print(arr4Linspace)
print()


randArr = np.random.randint(1,21,(5,4))
print(randArr)
print()
print(randArr.min())
print(randArr.max())
print(randArr.mean())
print(randArr.sum())
print()
print('0 axis')
print(randArr.min(axis=0)) # axis 0 = Spaltenweise Minimas als Array
print(randArr.max(axis=0))
print(randArr.mean(axis=0))
print(randArr.sum(axis=0))
print()
print('1 axis')
print(randArr.min(axis=1))
print(randArr.max(axis=1))
print(randArr.mean(axis=1))
print(randArr.sum(axis=1))

# 2d array to many arrays
def transformArr(arr: np.ndarray) -> list[np.ndarray]:
    arrList = []
    elements = arr.shape[0] * arr.shape[1]
    
    #1d array
    arrList.append(arr.reshape(elements))
    
    #2d arrays
    for i in range(2,elements):
        if elements % i == 0:
            arrList.append(arr.reshape(i, elements//(i)))
    
    #3d arrays
    for i in range(2,elements):
        if elements % i == 0:
            for j in range(2,elements//i):
                if (elements//i) % j == 0:
                    arrList.append(arr.reshape(i,j, elements//(i*j)))
    return arrList

print('transformArr')
for arr in transformArr(randArr):
    print(arr)
    print()