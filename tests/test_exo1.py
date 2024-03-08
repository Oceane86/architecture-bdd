<<<<<<< HEAD
# Écrivez un programme Python qui accepte une chaîne de caractères de l'utilisateur et affiche le nombre de majuscules et de minuscules.

=======
>>>>>>> e658f4d4b028c394129fa9ddf054f133337b6cbb
import pytest


def count_letters(chaine):
    majuscules = 0
    minuscules = 0

    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1
        elif caractere.islower():
            minuscules += 1

    return majuscules, minuscules


@pytest.mark.parametrize("input_string, expected_counts", [
    ("OK", (2, 0)),
    ("ok", (0, 2)),
    ("HelloWorld", (2, 8)),
    ("AbCdEf", (3, 3)),
    ("123", (0, 0)),
    ("", (0, 0)),
])
def test_count_letters(input_string, expected_counts):
    result = count_letters(input_string)
    assert result == expected_counts
