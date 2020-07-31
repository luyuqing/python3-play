# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/


def lazy_range(up_to):
    index = 0
    while index < up_to:
        yield index
        index += 1


# iterator1 = lazy_range(5)
# print(next(iterator1))
# print(next(iterator1))
# for x in iterator1:
#     print(x)


def jumping_range(up_to):
    """
    Generator for the sequence of integers from 0 to up_to, exclusive.
    Sending a value into the generator will shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        print("jump is: ", jump)
        if jump is None:
            jump = 1
        index += jump


iter2 = jumping_range(10)

# print(next(iter2))
# print(next(iter2))
# print(iter2.send(5))
# print(next(iter2))
# print(iter2.send(-1))
# print(next(iter2))


# yield from, also lets you chain generators together
def func1(up_to):
    index = 0

    def func2():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from func2()


gen = func1(10)
print(next(gen))
print(next(gen))
