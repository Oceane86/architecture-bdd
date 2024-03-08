# Écrivez un programme Python qui prend une liste et retourne une nouvelle liste 
# contenant uniquement les éléments uniques de la première liste.

import pytest


def unique_elements(lst):
    return list(set(lst))


@pytest.mark.parametrize("input_list, resultat", [
    ([1, 2, 3, 4, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([], []),
    (["a", "b", "a", "c"], ["a", "b", "c"]),  
    ([1, 1, 1, 1], [1]),
])
def test_unique_elements(input_list, resultat):
    result = unique_elements(input_list)
    assert sorted(result) == sorted(resultat)  
