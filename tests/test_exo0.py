# Écrivez un programme Python qui accepte une chaîne de caractères de l'utilisateur et affiche le nombre de majuscules et de minuscules.

import pytest


def addition(a, b):
    return a + b


@pytest.mark.parametrize("a, b, r", [(10, 8, 18), (-5, -10, -15)])
def test_add_two_numbers(a, b, r):
    print(f"La somme de a={a}, b={b}, est égale à={r}")
    assert addition(a, b) == r