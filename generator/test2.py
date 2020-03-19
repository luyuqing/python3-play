# def test():
#     yield 2
#     return 3

# t = test()
# print(next(t))  # 2
# print(next(t))  # exception value 3


# def test():
#     print((yield 2))
#     return 3

# t = test()
# print(next(t))  # 2
# print(next(t))  # None; exception value 3


# def test():
#     print((yield 2))
#     return 3

# t = test()
# print(next(t))  # 2
# print(t.send('abc'))  # abc; exception value 3


def inner():
    print((yield 2))
    return 3


def outer():
    yield 1
    val = yield from inner()
    print('val is: {}'.format(val))
    yield 4


gen = outer()
print(next(gen))  # 1
print(next(gen))  # 2
print(gen.send('abc'))  # abc, val is: 3, 4
