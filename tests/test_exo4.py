# Vous disposez de la chaîne de caractères suivante : "Python est un langage de programmation puissant et facile à apprendre."
# Extraction simple : Extraire le mot "Python" de la chaîne.
# Extraction par indices négatifs : Extraire le mot "apprendre" en utilisant des indices négatifs.
# Slicing : Extraire la phrase "langage de programmation" en utilisant le slicing.
# Challenge : Inversez la chaîne de caractères entière.
import pytest


def inverser_chaine(chaine):
    return chaine[::-1]


@pytest.mark.parametrize("chaine, chaine_inversee", [
    ("Python est un langage de programmation puissant et facile à apprendre", "erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP"),
])
def test_inversion(chaine, chaine_inversee):
    resultat = inverser_chaine(chaine)
    assert resultat == chaine_inversee
