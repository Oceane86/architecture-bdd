
# Écrivez un programme qui retourne la différence symétrique entre deux ensembles.
import pytest


@pytest.mark.parametrize("ensemble1, ensemble2, expected_result", [
    ({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}, {1, 2, 6, 7}),
    ({1, 2, 3}, {4, 5, 6}, {1, 2, 3, 4, 5, 6}),
    ({}, {1, 2, 3}, {1, 2, 3}),
    (set(), set(), set()),
])
def test_difference_symetrique(ensemble1, ensemble2, expected_result):
    """Test the difference symetrique method."""
    assert ensemble1.diff_sym(ensemble2) == expected_result 
