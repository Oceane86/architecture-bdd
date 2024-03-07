import unittest

class TestLettre(unittest.TestCase):

    def test_count_majuscule(self):
        self.assertEqual(count_letters("ok"), 2)
        self.assertEqual(count_letters("OK"), 2)
        self.assertEqual(count_letters(""), 0)

    def test_count_minuscule(self):
        self.assertEqual(count_letters("ok"), 2)
        self.assertEqual(count_letters("ok"), 0)
        self.assertEqual(count_letters(""), 0)

def count_letters(chaine):
    majuscules = 0
    minuscules = 0

    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1
        elif caractere.islower():
            minuscules += 1

    return majuscules, minuscules

if __name__ == '__main__':
    unittest.main()