ergebnisse = []
for i in range(25):
    ergebnisse.append(0)
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                ergebnisse[i+j+k+l]+=1
for i in range(4,25):
    print(str(i)+"\t"+str(ergebnisse[i]))