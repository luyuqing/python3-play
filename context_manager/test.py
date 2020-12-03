from contextlib import contextmanager 


@contextmanager
def con(*args, **kwargs):
    a = 0
    for x in args:
        a += x
    for _, v in kwargs.items():
        a += v**2
        
    try:
        print(a)
        yield
    finally:
        a = 0
        print(a)


with con(1, 2, m=3):
    print("here")