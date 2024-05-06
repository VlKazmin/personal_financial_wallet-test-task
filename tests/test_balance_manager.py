import pytest

from src.balance.balance_manager import BalanceManager


@pytest.fixture
def balance_manager():
    return BalanceManager("data/test_database.json")

def test_initial_balance(balance_manager, capsys):
    balance_manager.current_balance()
    captured = capsys.readouterr()
    assert "Текущий баланс: 200.0" in captured.out

def test_expense_balance(balance_manager, capsys):
    balance_manager.current_balance(show_expense=True)
    captured = capsys.readouterr()
    assert "Расходы: 500.0" in captured.out.strip()

def test_income_balance(balance_manager, capsys):
    balance_manager.current_balance(show_income=True)
    captured = capsys.readouterr()
    assert "Доходы: 700.0" in captured.out.strip()
