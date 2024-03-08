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
