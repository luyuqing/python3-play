from typing import (
    Any,
    Dict,
    Iterable,
    Tuple,
    Sequence,
    Optional,
    Union,
    List,
    Set,
    TypeVar,
    Generic
)


# 1
def test(n: Optional[str]):
    return 5


test(None)


# 2
X = TypeVar('X')


def flatten(values: Iterable[Union[Optional[X], List[X], Tuple[X]]]) -> Set[X]:
    """
    Flattens non-None values into a set.
    """
    out = set()  # type: Set[X]

    for value in values:
        if value is None:
            continue

        if isinstance(value, (tuple, list)):
            out.update(flatten(value))
            continue

        out.add(value)

    return out


print(flatten([2, 5, ['g', 78]]))


# 3
def test2(n: X) -> X:
    return n


def test3(n: X) -> X:
    return n


test2(5)  # OK
test3("ss")  # OK


# 4
class Test(Generic[X]):
    def func_1(self, n: X) -> X:
        return n

    def func_2(self, n: X) -> X:
        return n


t = Test()  # type: Test[int]
# print(t.func_1(1))  # OK
# print(t.func_2('a'))  # mypy error incompatible type "str"; expected "int"


# 5
Args = Tuple[Any, ...]


def test5(args: Args):
    return 123


print(test5(1))  # error: Argument 1 to "test5" has incompatible type "int"; expected "Tuple[Any, ...]"
# mypy --show-error-codes test.py
print(test5(1))  # type: ignore [arg-type]
print(test5((1, "kk")))


# 6
def test_dict(x: Dict[str, list]):
    return x


test_dict({"a": 2})  # error: Dict entry 0 has incompatible type "str": "int"; expected "str": "List[Any]"
