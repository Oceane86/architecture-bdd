import unittest
import pytest


def addition(a, b):
    return a + b

@pytest.mark.parametrize("a, b, r", [(10, 8, 18), (-5, -10, -15), (2.5, 3.5, 6.0)])
def test_add_two_numbers(a, b, r):
        print(f"La somme de a={a}, b={b}, est égale à={r}")
        assert addition(a, b) == r