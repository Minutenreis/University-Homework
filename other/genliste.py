def genListe(n):
    if(n<0):
        n = -n
    list = []
    i = 1
    while(i <= n):
        list.append(i**2)
        i += 1
    return list

print(genListe(5))
print(genListe(0))
print(genListe(-5))
