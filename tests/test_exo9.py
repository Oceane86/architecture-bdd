
import unittest

def reverse_tuples(tuples):
    reversed_tuples = []

    for t in tuples:
        reversed_tuples.append(tuple(reversed(t)))

    return reversed_tuples

class TestReverseTuples(unittest.TestCase):

    def test_reverse_tuples(self):
        tuples = [(1, 2), (1, 2, 3), (1, 2)]
        expected = [(2, 1), (3, 2, 1), (2, 1)]

        self.assertEqual(reverse_tuples(tuples), expected)

if __name__ == '__main__':
    unittest.main()