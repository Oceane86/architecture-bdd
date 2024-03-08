# Écrivez un programme Python qui effectue une rotation à droite des éléments 
# d'une liste. La rotation doit être définie par l'utilisateur.

import pytest


def rotate_list(lst, x):
    n = len(lst)
    if n == 0:
        return lst

    x = x % n  
    return lst[-x:] + lst[:-x]


class TestRotationListe:

    @pytest.mark.parametrize("liste, x, expected", [
        ([1, 2, 3, 4, 5, 6], 2, [5, 6, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3]),
        ([], 2, []),
        (['a', 'b', 'c', 'd'], 1, ['d', 'a', 'b', 'c']),
        ([1, 2, 3, 4, 5, 6], -1, [2, 3, 4, 5, 6, 1]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 5, [4, 5, 6, 7, 8, 1, 2, 3]),
    ])
    def test_rotation(self, liste, x, expected):
        new_liste = rotate_list(liste, x)
        assert new_liste == expected


if __name__ == '__main__':
    pytest.main([__file__])
