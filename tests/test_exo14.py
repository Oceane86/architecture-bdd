import pytest


def modifier_element(byte_array, index, nouvelle_valeur):
    byte_array[index] = nouvelle_valeur
    return byte_array


@pytest.mark.parametrize("liste_entiers, index_modification, nouvelle_valeur, resultat", [
    ([65, 66, 67, 68, 69], 2, 70, bytearray([65, 66, 70, 68, 69])),
    ([10, 20, 30, 40, 50], 3, 25, bytearray([10, 20, 30, 25, 50])),
    ([1, 2, 3, 4, 5], 0, 100, bytearray([100, 2, 3, 4, 5])),
])
def test_modifier_element(liste_entiers, index_modification, nouvelle_valeur, resultat):
    byte_array = bytearray(liste_entiers)
    result = modifier_element(byte_array, index_modification, nouvelle_valeur)
    assert result == resultat


if __name__ == "__main__":
    pytest.main([__file__])
