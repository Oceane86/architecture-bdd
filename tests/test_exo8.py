import unittest

class TestTupleWithMostElements(unittest.TestCase):

    def test_tuple_with_most_elements(self):
        tuples = [(1, 2), (1, 2, 3)]
        for t in tuples:
            self.assertEqual(t + (None, None), tuple.__new__(tuple, list(t) + [None, None]))   
            if __name__ == '__main__':
                print("Passed")

if __name__ == '__main__':
    unittest.main()