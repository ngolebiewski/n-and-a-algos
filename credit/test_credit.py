# test_credit.py

import pytest
from credit import main


def run_card(monkeypatch, capsys, number):
    """Run the program with a mocked input and return printed output."""
    monkeypatch.setattr("builtins.input", lambda _: str(number))
    main()
    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "number,expected",
    [
        # AMEX
        (378282246310005, "AMEX"),
        (371449635398431, "AMEX"),

        # MasterCard
        (5555555555554444, "MASTERCARD"),
        (5105105105105100, "MASTERCARD"),

        # Visa
        (4111111111111111, "VISA"),
        (4012888888881881, "VISA"),
        (4222222222222, "VISA"),

        # Invalid
        (1234567890, "INVALID"),
        (369421438430814, "INVALID"),
        (4062901840, "INVALID"),
        (5673598276138003, "INVALID"),
        (4111111111111113, "INVALID"),
        (4222222222223, "INVALID"),
        (3400000000000620, "INVALID"),
        (430000000000000, "INVALID"),
    ],
)
def test_credit_cards(monkeypatch, capsys, number, expected):
    assert run_card(monkeypatch, capsys, number) == expected