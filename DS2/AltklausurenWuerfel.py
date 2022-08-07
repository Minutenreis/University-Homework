count = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                for m in range(1,7):
                    if(i+j+k+l+m == 24):
                        count+=1
print(count)