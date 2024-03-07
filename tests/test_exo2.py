import unittest

class TestExtractionMots(unittest.TestCase):

    def test_extraction(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        mots = chaine.split()
        python = mots[0]

        self.assertEqual(python, 'Python')

if __name__ == '__main__':
    unittest.main()


