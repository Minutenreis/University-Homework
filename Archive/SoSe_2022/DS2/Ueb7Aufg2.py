count = 0
for i in range(0, 11):
    for j in range(0, 11-i):
        for k in range(0, 11-i-j):
            if((i!=0) | (j!=0) | (k!=0)):
                count+= 1
print(count)
