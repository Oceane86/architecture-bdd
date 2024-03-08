#  Implémentez le parcours en profondeur (DFS) sur un graphe représenté par un dictionnaire.

import pytest


def dfs(graphe, sommet, visite=set()):
    if sommet not in visite and sommet in graphe:
        visite.add(sommet)
        for voisin in graphe[sommet]:
            dfs(graphe, voisin, visite)

      
@pytest.mark.parametrize("graphe, sommet_depart, resultat_attendu", [
    ({'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}, 'A', {'A', 'B', 'D', 'C', 'E'}),
    ({'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}, 'B', {'B', 'D'}),
    ({'A': ['B'], 'B': ['A']}, 'A', {'A', 'B'}),
    ({'A': ['B'], 'B': ['A']}, 'C', {'C'}),
])
def test_dfs(graphe, sommet_depart, resultat_attendu):
    visite = set()
    if sommet_depart in graphe:
        dfs(graphe, sommet_depart, visite)
    assert visite == resultat_attendu, f"Résultat obtenu: {visite}, Résultat attendu: {resultat_attendu}"


if __name__ == "__main__":
    pytest.main([__file__])
