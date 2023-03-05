count = 0
for x1 in range(0,7):
    for x2 in range(0,7):
        for x3 in range(0,7):
            for x4 in range(0,7):
                if(x1+x2+x3+x4 == 18):
                    count += 1
print(count)