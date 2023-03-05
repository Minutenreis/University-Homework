import random

def checkList(list):
    for elem in list:
        x = elem
        for i in range(51):
            if(i == 50):
                return False
            x = list[x]
            if(x == elem):
                break
    return True

list = []
countTrue = 0
repeats = 100000
for i in range(100):
    list.append(i)
for i in range(repeats):
    random.shuffle(list)
    if(checkList(list)):
        countTrue += 1
print(countTrue / repeats)
