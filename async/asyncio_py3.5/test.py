# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/


# The problem with this, though, is that if you want a large sequence like the integers from 0 to 1,000,000,
# you have to create a list long enough to hold 1,000,000 integers.
def eager_range(up_to):
    """Create a list of integers, from 0 to up_to, exclusive."""
    sequence = []
    index = 0
    while index < up_to:
        sequence.append(index)
        index += 1
    return sequence


# Now comes generator
def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    while index < up_to:
        yield index
        index += 1


# PEP 342 introduced the send() method on generators.
# This allowed one to not only pause generators, but to send a value back into a generator where it paused.
def jumping_range(up_to):
    index = 0
    while index <= up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump


iterator = jumping_range(10)
print(next(iterator))  # 0
print(next(iterator))  # 1
print(iterator.send(6))  # 7


# By virtue of making refactoring easier,
# yield from also lets you chain generators together so that values bubble up and down the call stack
# without code having to do anything special.
def my_range(up_to):
    index = 0

    def refactor():
        nonlocal index
        while index <= up_to:
            yield index
            index += 1
    yield from refactor()


my_ran = my_range(10)
print(next(my_ran))  # 0
print(next(my_ran))  # 1


""" compare below 2 examples carfully"""


# Example 1
def bottom():
    yield 35


def middle():
    yield from bottom()


def top():
    yield from middle()


gen = top()
value = next(gen)
print(value)  # 35

try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value

print(value)  # None


# Example 2
def bottom2():
    return(yield 35)


def middle2():
    return(yield from bottom2())


def top2():
    return(yield from middle2())


gen = top2()
value = next(gen)
print(value)  # 35

try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value

print(value)  # 70
