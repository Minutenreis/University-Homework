def h1(k): return k % 11
def h2(k): return 1 + (k % 10)
def hDouble(k, i): return (h1(k) + i * h2(k)) % 11
def hLinear(k, i): return (h1(k) + i) % 11


def insert(T, k, h=hLinear):
    for i in range(11):
        j = h(k, i)
        if T[j] == None:
            T[j] = k
            return j
    return None


def hash(T, List, h=hLinear):
    for i in range(len(List)):
        insert(T, List[i], h)
    return T


print("Linear:", hash([None]*11, [42, 14, 83, 25, 66, 37, 33, 38], hLinear))
print("Double:", hash([None]*11, [42, 14, 83, 25, 66, 37, 33, 38], hDouble))
