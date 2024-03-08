import pytest
# Écrivez un programme qui crée un bytearray à partir d'une liste d'entiers, puis modifie un de ses éléments.
def modifier_element(byte_array, index, new_valeur):
    byte_array[index] = new_valeur
    return byte_array


@pytest.mark.parametrize("liste_entiers, index_modification, new_valeur, resultat", [
    ([255, 0, 128], 1, 200, bytearray([255, 200, 128])),  
])
def test_modifier_element_autres_scenarios(liste_entiers, index_modification, new_valeur, resultat):
    byte_array = bytearray(liste_entiers)
    result = modifier_element(byte_array, index_modification, new_valeur)
    assert result == resultat
