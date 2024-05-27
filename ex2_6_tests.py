import pytest

from ex2_6 import BankAccount

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

    with pytest.raises(ValueError):
        BankAccount(-100)


def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

    with pytest.raises(ValueError):
        account.deposit(-50)

    with pytest.raises(ValueError):
        account.deposit(0)


def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

    with pytest.raises(ValueError):
        account.withdraw(-50)

    with pytest.raises(ValueError):
        account.withdraw(0)

    with pytest.raises(ValueError):
        account.withdraw(200)


def test_get_balance():
    account = BankAccount(150)
    assert account.get_balance() == 150

    account.deposit(50)
    assert account.get_balance() == 200

    account.withdraw(100)
    assert account.get_balance() == 100