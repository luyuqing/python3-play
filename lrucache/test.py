from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(9))


# equivalent to below
def fib2(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

func = lru_cache(maxsize=None)(fib2)
print(func(9))

