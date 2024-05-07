
def rekursion(n=0):
    try:
        return rekursion(n+1)
    except RecursionError:
        return n

print(rekursion())

def Range2(n):
    i = 0
    while i < n:
        yield i
        i += 1