count = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                if(i+j+k+l == 18):
                    count+=1          
print(count)