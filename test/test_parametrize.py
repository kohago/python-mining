
import pytest

@pytest.mark.parametrize(
    "x,y", [
    ("aaa","bbb"),
    ("aaa","aaa"),
    ("bbb","bbb")
    ]
)

def test_1(x,y):
    assert x == y
