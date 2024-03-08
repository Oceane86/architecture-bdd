# Étant donné un dictionnaire contenant le nom des étudiants et leurs notes moyennes, 
# écrivez un programme qui génère un nouveau dictionnaire avec les noms des étudiants 
# qui ont une note moyenne supérieure ou égale à 15.


import pytest


def filtrer_etudiants(notes):
    etudiants_reussite = {nom: note for nom, note in notes.items() if note >= 15}
    return etudiants_reussite


@pytest.mark.parametrize("notes, resultat_attendu", [
    ({'Alice': 18, 'Bob': 12, 'Charlie': 16, 'David': 14, 'Eva': 20}, {'Alice': 18, 'Charlie': 16, 'Eva': 20}),
    ({'John': 14, 'Emma': 15, 'Michael': 10, 'Sophie': 18}, {'Emma': 15, 'Sophie': 18}),
    ({}, {}),
])
def test_filtrer_etudiants(notes, resultat_attendu):
    result = filtrer_etudiants(notes)
    assert result == resultat_attendu


if __name__ == "__main__":
    pytest.main([__file__])
