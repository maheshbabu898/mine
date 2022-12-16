import add
import pytest


def test_add_even_ans():
    assert add.add_even_ans([2, 3]) == 2
    assert add.add_even_ans([-2, 2]) == 0


def test_good_add_up():
    assert add.actual_good_add_up(-6) == -12
