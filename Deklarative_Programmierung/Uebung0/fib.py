def fibIter(a, b, count):
    if count == 0:
        return b
    else:
        return fibIter(a+b, a, count-1)


def fib(n):
    return fibIter(1, 0, n)


print(fib(10))
print("\n")
