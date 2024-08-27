paare = ['AT','TA','CG','GC']
perm = [0,0,0,0,0]
while perm != [3,3,3,3,3]:
    print(paare[perm[0]],paare[perm[1]],paare[perm[2]],paare[perm[3]],paare[perm[4]])
    perm[4] += 1
    for i in range(4,-1,-1):
        if perm[i] == 4:
            perm[i] = 0
            perm[i-1] += 1
print(paare[3],paare[3],paare[3],paare[3],paare[3])