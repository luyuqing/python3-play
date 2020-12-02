import pytest


@pytest.fixture(scope='module')
def test_t1():
    a = 1
    yield a
    print("here")


def test_t2():
    assert 2 == 2