import pytest


def unique_element(lst):
    return list(set(lst))


@pytest.mark.parametrize("input_list, resultat", [
    ([1, 2, 3, 4, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 1, 1, 1, 1], [1]),  
    ([], []),  
])
def test(input_list, resultat):
    result = unique_element(input_list)
    assert result == resultat