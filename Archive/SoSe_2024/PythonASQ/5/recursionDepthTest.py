
def rekursion(n=0):
    try:
        return rekursion(n+1)
    except RecursionError:
        return n

print(rekursion())