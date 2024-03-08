import pytest


def main_with_input(input_values):
    numero1str = input_values[0]
    numero2str = input_values[1]

    numero1 = int(numero1str)
    numero2 = int(numero2str)

    somme = numero1 + numero2

    return somme


@pytest.mark.parametrize("user_input, expected_output", [
    (("5", "7"), 12),
    (("0", "0"), 0),  
    (("-5", "5"), 0), 
    (("1000", "500"), 1500),  
])
def test_sum(user_input, expected_output):
    result = main_with_input(user_input)
    assert result == expected_output


def test_invalid_input():
    with pytest.raises(ValueError):
        main_with_input(("abc", "7"))  


if __name__ == "__main__":
    pytest.main([__file__])
