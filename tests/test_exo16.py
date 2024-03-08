# Écrivez un programme pour représenter un graphe en utilisant un dictionnaire en Python.

import pytest


def parcourir_graphe(graphe, depart):
    parcours = []
    file_attente = [depart]
    deja_vu = set()

    while file_attente:
        sommet = file_attente.pop(0)
        if sommet not in deja_vu:
            parcours.append(sommet)
            deja_vu.add(sommet)
            file_attente.extend(graphe[sommet])

    return parcours

# Paramètres de test


@pytest.mark.parametrize("graphe, depart, resultat_attendu", [
    ({'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}, 'A', ['A', 'B', 'C', 'D', 'E']),
    ({'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}, 'B', ['B', 'D']),
    ({'A': ['B'], 'B': ['A']}, 'A', ['A', 'B']),
])
def test_parcourir_graphe(graphe, depart, resultat_attendu):
    result = parcourir_graphe(graphe, depart)
    assert result == resultat_attendu


if __name__ == "__main__":
    pytest.main([__file__])
