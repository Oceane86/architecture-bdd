import pytest


def inverser_chaine(chaine):
    return chaine[::-1]


@pytest.mark.parametrize("chaine, chaine_inversee", [
    ("Python est un langage de programmation puissant et facile à apprendre", "erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP"),
])
def test_inversion(chaine, chaine_inversee):
    resultat = inverser_chaine(chaine)
    assert resultat == chaine_inversee
