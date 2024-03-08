# import pytest
# from programme_pyramide import afficher_pyramide


# @pytest.mark.parametrize("hauteur, expected_output", [
#     (3, "  *\n ***\n*****\n"),
#     (5, "    *\n   ***\n  *****\n *******\n*********\n"),
#     (1, "*\n"),
# ])
# def test_afficher_pyramide(hauteur, expected_output, capsys):
#     afficher_pyramide(hauteur)
#     captured = capsys.readouterr()
#     assert captured.out == expected_output


# @pytest.mark.parametrize("hauteur", [-1, 0, -5])
# def test_afficher_pyramide_hauteur_invalide(hauteur, capsys):
#     with pytest.raises(ValueError, match="La hauteur de la pyramide doit être un entier positif"):
#         afficher_pyramide(hauteur)


# @pytest.mark.parametrize("hauteur, expected_output", [
#     (4, "   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n"),
# ])
# def test_afficher_pyramide_even_rows(hauteur, expected_output, capsys):
#     afficher_pyramide(hauteur)
    captured = capsys.readouterr()
    assert captured.out == expected_output
