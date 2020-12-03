import pytest


@pytest.fixture(scope='module', autouse=True)
def test_t1():
    print("t1")
    a = 1
    yield a
    print("t1 after yield")


def test_t2(test_t1):
    print("t2")
    assert test_t1 == 1