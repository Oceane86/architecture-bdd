import unittest

class TestRotationListe(unittest.TestCase):

    def test_rotation(self):
        liste = [1, 2, 3, 4, 5, 6]
        x = 2
        new_liste = liste[int(x):] + liste[0:int(x)]
        expected = [3, 4, 5, 6, 1, 2]

        self.assertEqual(new_liste, expected)

        liste = [1, 2, 3, 4, 5, 6]
        x = 3
        new_liste = liste[int(x):] + liste[0:int(x)]
        expected = [4, 5, 6, 1, 2, 3]

        self.assertEqual(new_liste, expected)

if __name__ == '__main__':
    unittest.main()