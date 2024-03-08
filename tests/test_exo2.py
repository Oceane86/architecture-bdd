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
