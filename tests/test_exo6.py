import unittest

def unique_elements(lst):
    return list(set(lst))

class TestUniqueElements(unittest.TestCase):

    def test_unique_elements(self):
        lst = [1, 2, 3, 4, 4, 5, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]

        self.assertEqual(unique_elements(lst), expected)

if __name__ == '__main__':
    unittest.main()