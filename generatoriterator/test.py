"""Iterator"""
# echnically speaking, a Python iterator object must implement two special methods,
# __iter__() and __next__(),collectively called the iterator protocol.
# i found actually list, tuple, etc. has __iter__ then has __next__ for the iter part, not implemeted at the same time
# lst = [...] dir(lst) has __iter__ but not __next__
# An object is called iterable if we can get an iterator from it. (if we can do for .. in ..)


# An example without __next__
class MyIterObj():
    def __init__(self):
        self._list = [1, 2, 'a']

    def __iter__(self):
        return iter(self._list)


obj = MyIterObj()
for x in obj:
    print(x)  # 1 2 a


# An example with __next__
class PowTwo():
    def __init__(self, m=0):
        self.max = m

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


p = PowTwo(3)
for x in p:
    print(x)  # 1 2 4 8


"""generator"""
"""generator implement iterator protocol"""


# Generator function contains one or more yield statements.
def my_gen():
    n = 0
    yield n
    n += 1
    yield n

g = my_gen()
print(next(g))  # 0
print(next(g))  # 1
# print(next(g))  # Stop Iteration error


# Generator with a loop
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


rev_g = rev_str('hello')
for char in rev_g:
    print(char)  # o l l e h


# Simple generator expression
lst = [1, 2, 'abc']
gen = (x for x in lst)
print(gen)  # <generator object <genexpr> at 0x7f8475ac65c8>


# Using generator to replace iterator example above PowTwo
def pow_two(max_n=0):
    n = 0
    while n <= max_n:
        yield 2 ** n
        n += 1


gen = pow_two(3)
for x in gen:
    print(x)  # 1 2 4 8


"""Continue generator in asyncio/test.py"""
