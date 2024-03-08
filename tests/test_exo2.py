# Vous disposez de la chaîne de caractères suivante : "Python est un langage de programmation puissant et facile à apprendre."
# Extraction simple : Extraire le mot "Python" de la chaîne.
# Extraction par indices négatifs : Extraire le mot "apprendre" en utilisant des indices négatifs.
# Slicing : Extraire la phrase "langage de programmation" en utilisant le slicing.
# Challenge : Inversez la chaîne de caractères entière.
import pytest


def extraction(chaine):
    mots = chaine.split()
    return mots[0]


@pytest.mark.parametrize("input_string, expected_result", [
    ("Python est un langage de programmation puissant et facile à apprendre", "Python"),
])
def test_extraction(input_string, expected_result):
    result = extraction(input_string)
    assert result == expected_result
