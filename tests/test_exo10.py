import unittest
import random

def guess_the_number(max_attempts=5):
    number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in {} attempts!".format(attempts))
            return

    print("Sorry, you didn't guess the number in {} attempts.".format(max_attempts))

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