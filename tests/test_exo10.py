import unittest
import random

def guess_the_number(max_attempts=5):
    number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = int(input("Trouve le nombre: "))
        attempts += 1

        if guess < number:
            print("Trop bas")
        elif guess > number:
            print("Trop haut!")
        else:
            print("C'est le bon nombre ! Il reste {} tentatives!".format(attempts))
            return

    print("Désolé, vous n'avez pas trouver {} tentatives.".format(max_attempts))

class TestGuessTheNumber(unittest.TestCase):

    def test_guess_the_number(self):
        random.seed(0)  

        max_attempts = 1
        number = 42
        input_mock = unittest.mock.Mock()
        input_mock.side_effect = [number]
        with unittest.mock.patch('builtins.input', input_mock):
            guess_the_number(max_attempts)

        max_attempts = 5
        number = 7
        input_mock = unittest.mock.Mock()
        input_mock.side_effect = [6, 8, 7]
        with unittest.mock.patch('builtins.input', input_mock):
            guess_the_number(max_attempts)

        max_attempts = 3
        number = 42
        input_mock = unittest.mock.Mock()
        input_mock.side_effect = [10, 20, 30]
        with unittest.mock.patch('builtins.input', input_mock):
            guess_the_number(max_attempts)

if __name__ == '__main__':
    unittest.main()