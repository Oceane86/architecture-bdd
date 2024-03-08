# Écrivez un programme qui trouve l'intersection de deux ensembles.


# import pytest
from programme_intersection import trouver_intersection

@pytest.mark.parametrize("ensemble1, ensemble2, expected_result", [
    ({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}, {3, 4, 5}),
    ({1, 2, 3}, {4, 5, 6}, set()),
    ({}, {1, 2, 3}, set()),
    (set(), set(), set()),
])
def test_trouver_intersection(ensemble1, ensemble2, expected_result):
    resultat_intersection = trouver_intersection(ensemble1, ensemble2)
    assert resultat_intersection == expected_result

@pytest.mark.parametrize("ensemble1, ensemble2", [
    ({1, 2, 3}, "non_ensemble"),
    ("non_ensemble", {4, 5, 6}),
])
def test_trouver_intersection_avec_types_invalides(ensemble1, ensemble2):
    with pytest.raises(TypeError):
        trouver_intersection(ensemble1, ensemble2)
