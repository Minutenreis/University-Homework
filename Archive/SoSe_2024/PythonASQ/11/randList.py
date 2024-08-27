import random, time, numpy as np


    

def make_random_list_randint(n: int):
    return [random.randint(0, 1000) for _ in range(n)]

def make_random_list_choices(n: int):
    return random.choices(range(1001), k=n)

def make_random_list_numpy(n: int):
    return np.random.randint(0, 1001, n)

def make_random_list_randrange(n: int):
    return [random.randrange(1001) for _ in range(n)]

if __name__ == "__main__":
    n = 10000
    
    start = time.time()
    make_random_list_randint(n)
    print("randint:", time.time() - start)
    
    start = time.time()
    make_random_list_choices(n)
    print("choices:", time.time() - start)
    
    start = time.time()
    make_random_list_numpy(n)
    print("numpy:  ", time.time() - start)
    
    start = time.time()
    make_random_list_randrange(n)
    print("randrange:", time.time() - start)