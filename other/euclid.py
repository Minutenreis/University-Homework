a = 160
b = 17

aArr = [a]
bArr = [b]
eArr = []
fArr = []
i = 0
while bArr[i] != 0:
    eArr.append(aArr[i] // bArr[i])
    fArr.append(aArr[i] % bArr[i])
    aArr.append(bArr[i])
    bArr.append(fArr[i])
    i += 1
ggt = aArr[i]
myArr = [1,0]
phiArr = [0,1]
for j in range(1,i):
    myArr.append(myArr[j-1] - eArr[j-1] * myArr[j])
    phiArr.append(phiArr[j-1] - eArr[j-1] * phiArr[j])

print("ggT(" + str(a) + "," + str(b) + ") = " + str(ggt))
print("my = " + str(myArr[i]) + " and phi = " + str(phiArr[i]))

