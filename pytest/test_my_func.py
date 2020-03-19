from my_func import add, multiply, square
import pytest
import sys


# pytest -v -rxs --capture=no(will print)
# pytest -k mul    just select the function name including mul
# pytest systemtest/tests --lf   will rerun only the tests that failed in the previous run.
# pytest systemtest/tests --ff   will run all tests, but the previously failed tests will be run first.

# pytest -n auto  (multi core, paralell test)


# @pytest.mark.skip(reason='I wannt test skip it')
# @pytest.mark.skipif(sys.version_info > (3, 3), reason='I wanna test this!')
@pytest.mark.mac
def test_add():
    total = add(8, 9)
    assert total == 17


@pytest.mark.ubuntu     # run:  pytest -m ubuntu -v OR  pytest -m "not windows" -v
def test_mul():
    res = multiply(2, 3)
    assert res == 6


# @pytest.fixture(params=[
#     {"input": 2, "output": 4},
#     {"input": 7, "output": 49}
# ])
@pytest.mark.parametrize("input, output",
                         [
                             (5, 25),
                             (3, 9),
                             (6, 36)
                         ])
def test_square(input, output):
    res = square(input)
    assert res == output


# only open connection once
# @pytest.fixture(scope="module")
# def cur():
#     db = MyDB()
#     conn = db.connect("server")
#     curs = conn.cursor()
#     yield curs
#     curs.close()
#     conn.close()

# def test_jj(cur):
#     id = cur.execute("select id from user where name=jj")
#     assert id == 123

# def test_kk(cur):
#     id = cur.execute("select id from user where name=kk")
#     assert id == 789
