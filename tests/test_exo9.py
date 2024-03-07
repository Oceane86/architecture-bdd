import pytest


def reverse_tuples(tuples):
    inverser_tuples = []

    for t in tuples:
        inverser_tuples.append(tuple(reversed(t)))

    return inverser_tuples


@pytest.mark.parametrize("input_tuple, resultat", [
    ((1, 2), (2, 1)),
    ((1, 2, 3), (3, 2, 1)),
    ((1, 2), (2, 1)),
])
def test_reverse_tuples(input_tuple, resultat):
    result = reverse_tuples([input_tuple])
    assert result == [resultat]
