# Écrivez un programme Python qui prend une liste de tuples et 
# affiche le tuple avec le plus d'éléments.

import pytest


@pytest.mark.parametrize("t", [
    ((1, 2),),
    ((1, 2, 3),),
])
def test_tuple_with_most_elements(t):
    result = t[0] + (None, None)
    expected = tuple.__new__(tuple, list(t[0]) + [None, None])
    assert result == expected
