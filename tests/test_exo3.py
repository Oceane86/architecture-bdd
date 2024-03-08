# Vous disposez de la chaîne de caractères suivante : "Python est un langage de programmation puissant et facile à apprendre."
# Extraction simple : Extraire le mot "Python" de la chaîne.
# Extraction par indices négatifs : Extraire le mot "apprendre" en utilisant des indices négatifs.
# Slicing : Extraire la phrase "langage de programmation" en utilisant le slicing.
# Challenge : Inversez la chaîne de caractères entière.
import pytest


def extract_substring(chaine):
    mots = chaine.split()
    phrase = "_".join(mots[13:18])
    return phrase


@pytest.mark.parametrize("chaine, expected_phrase", [
    ("Python est un langage de programmation puissant et facile à apprendre", "langage_de_programmation"),
])
def test_extraction(chaine, expected_phrase):
    result = extract_substring(chaine)
    assert result == expected_phrase
