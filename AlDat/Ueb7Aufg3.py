def h1(k,m):
    return k % m

def h2(k,m):
    return 1 + k % (m-1)


def hLin(k,m,i):
    return (h1(k,m)+i) % m

def hDouble(k,m,i):
    return (h1(k,m)+i*h2(k,m)) % m

def hashList(m,K,hashFunc):
    M = [None] * m
    for elem in K:
        j=0
        linHash = hashFunc(elem,m,j)
        while M[linHash] != None:
            j+=1
            linHash = hashFunc(elem,m,j)
        M[linHash] = elem
    return M

K = [ 17, 23, 37, 6, 61, 103, 59, 91]
print("[", end = "")
print(*hashList(11,K,hLin), sep = "\t|", end= "]\n")
print()
print("[", end = "")
print(*hashList(11,K,hDouble), sep = "\t|", end= "]\n")




        