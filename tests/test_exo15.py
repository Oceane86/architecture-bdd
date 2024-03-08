# Écrivez un programme qui parcourt un bytearray, affiche chaque élément, puis ajoute 1 à chaque élément.

import pytest


def parcourir_et_incrementer(byte_array):
    for i, valeur in enumerate(byte_array):
        print(f"Élément {i + 1} : {valeur}")
        byte_array[i] += 1


@pytest.mark.parametrize("byte_array, resultat_attendu", [
    (bytearray([10, 20, 30, 40, 50]), bytearray([11, 21, 31, 41, 51])),
    (bytearray([5, 10, 15]), bytearray([6, 11, 16])),
    (bytearray([]), bytearray([])),
])
def test_parcourir_et_incrementer(byte_array, resultat_attendu):
    parcourir_et_incrementer(byte_array)
    assert byte_array == resultat_attendu


if __name__ == "__main__":
    pytest.main([__file__])
