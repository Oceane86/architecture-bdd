import unittest

class TestInversion(unittest.TestCase):

    def test_inversion(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        chaine_inversee = chaine[::-1]
        self.assertEqual(chaine_inversee, 'erendre appà laimargorp de gnolagnap era ucnu tse sihtoP')

if __name__ == '__main__':
    unittest.main()


