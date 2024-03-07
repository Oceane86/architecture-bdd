import pytest


def reverse_tuples(tuples):
    reversed_tuples = []

    for t in tuples:
        reversed_tuples.append(tuple(reversed(t)))

    return reversed_tuples


@pytest.mark.parametrize("input_tuple, expected_output", [
    ((1, 2), (2, 1)),
    ((1, 2, 3), (3, 2, 1)),
    ((1, 2), (2, 1)),
])
def test_reverse_tuples(input_tuple, expected_output):
    result = reverse_tuples([input_tuple])
    assert result == [expected_output]
