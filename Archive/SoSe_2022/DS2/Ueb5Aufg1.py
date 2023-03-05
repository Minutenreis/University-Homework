def containsDigit(number, digit):
    while(number>0):
        if ((number % 10) == digit):
            return True
        number=number // 10
    return False

countA = 0
countB = 0
for i in range(0,10000):
    if(containsDigit(i,3) & containsDigit(i,5) & containsDigit(i,2)):
        countA += 1
    if(containsDigit(i,3) | containsDigit(i,5) | containsDigit(i,2)):
        countB += 1
print("A:",countA)
print("B:",countB)


