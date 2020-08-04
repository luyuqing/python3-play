# @decorator_func
# def some_func()

# is equivalent to

# some_func = decorator_func(some_func)


import time
import math


def calc_time(func, repeat=1000):
    def inner(*args, **kwargs):
        resunt = None
        begin = time.time()
        for _ in range(repeat):
            result = func(*args, **kwargs)
        end = time.time()
        print("Result is {} used time {}".format(result, begin - end))
        print(func.__name__)  # fact
        return result  # try comment out, see difference

    return inner


@calc_time
def fact(num):
    return math.factorial(num)


fact(10)  # equivalent: calc_time(fact(10), repeat=1000)
print(fact.__name__)  # inner


# If using a decorator always meant losing this information about a function,
# it would be a serious problem. That's why we have
# functools.wraps
# This takes a function used in a decorator and adds the functionality of copying over the
# function name, docstring, arguments list, etc.

import functools


def calculate_time(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Result is {} used time {}".format(result, begin - end))
        return result  # can comment out, see difference

    return inner


@calculate_time
def fact2(num):
    """some docstings of fact2"""
    return math.factorial(num)


print(fact2.__name__)  # fact2
print(fact2.__doc__)  # some docstings of fact2
