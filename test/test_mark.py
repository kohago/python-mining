#python3 -m pytest -m small/larget test_mark.py
# => 1 passed, 2 deselected in 5.02 seconds

import pytest
import time

@pytest.mark.small
def test_1():
    time.sleep(0.1)
    assert "1" == "0"


@pytest.mark.small
def test_2():
    time.sleep(0.1)
    assert "1" == "1"


@pytest.mark.large
def test_3():
    time.sleep(5)
    assert "0" == "0"
