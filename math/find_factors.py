import itertools
from functools import reduce

def find_factors(n):
    c = list(range(1, n+1))
    l = []

    for i in range(1, n+1):
        temp_l = list(itertools.combinations(c, i))
        for k in temp_l:
            t = reduce(lambda x,y: x*y, k)
            if t not in l:
                l.append(t)
    
    return l, len(l)


def final(n):  # num is the number of factors
    x = 1
    num = 1
    while num < n:
        l, num = find_factors(x)
        x += 1
    
    return x-1, num


print(final(50))



