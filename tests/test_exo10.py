import pytest


def guess_the_number(max_attempts=5, input_function=input):
    number = 42
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input_function("Trouve le nombre: "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        attempts += 1

        if guess < number:
            print("Trop bas")
        elif guess > number:
            print("Trop haut!")
        else:
            print(f"C'est le bon nombre ! Il reste {max_attempts - attempts} tentatives.")
            return

    print(f"Désolé, vous n'avez pas trouvé {max_attempts} tentatives.")
    raise SystemExit

@pytest.mark.parametrize("input_values, expected_output", [
    (["42"], "C'est le bon nombre ! Il reste 4 tentatives."),
    (["dix", "10", "20", "30"], "Veuillez entrer un nombre valide."),
    (["10", "20", "30"], "Désolé, vous n'avez pas trouvé 5 tentatives."),
])
def test_guess_the_number_with_parametrize(capsys, input_values, expected_output, monkeypatch):
    input_values_iter = iter(input_values)
    monkeypatch.setattr('builtins.input', lambda _: str(next(input_values_iter, None)))

    with pytest.raises(SystemExit):
        guess_the_number()

    captured_output, _ = capsys.readouterr()
    assert captured_output.strip() == expected_output

if __name__ == '__main__':
    pytest.main([__file__])
