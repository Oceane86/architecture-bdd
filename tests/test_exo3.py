import unittest

class TestExtractionMots(unittest.TestCase):

    def test_extraction(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        mots = chaine.split()
        phrase = " ".join(mots[13:18])

        self.assertEqual(phrase, 'langage de programmation')




if __name__ == '__main__':
    unittest.main()
