from contextlib import contextmanager 


@contextmanager
def testcon():
    print("111")
    yield
    print("222")


with testcon():
    pass