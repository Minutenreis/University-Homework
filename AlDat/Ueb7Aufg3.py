from jinja2 import Undefined


def h1(k,m):
    return k % m

def h2(k,m):
    return 1 + k % (m-1)


def hLin(k,m,i):
    return (h1(k,m)+i) % m

def hDouble(k,m,i):
    return (h1(k,m)+i*h2(k,m)) % m

def hashList(m,K,hashFunc):
    M = []
    for i in range(m):
        M.append(' ')
    for i in range(len(K)):
        j=0
        linHash = hashFunc(K[i],m,j)
        while M[linHash] != ' ':
            j+=1
            linHash = hashFunc(K[i],m,j)
        M[linHash] = K[i]
        print("|", end = "")
        print(*M, sep = "\t|", end = "\t|\n")

K = [ 17, 23, 37, 6, 61, 103, 59, 91]
hashList(11,K,hLin)
print()
hashList(11,K,hDouble)




        