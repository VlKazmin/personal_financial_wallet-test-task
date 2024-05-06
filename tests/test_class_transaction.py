from datetime import date

from src.transactions.transaction import Transaction


def test_transaction_str():
    data = {
        "id": 1,
        "date": date(2024, 5, 5),
        "category": "доход",
        "amount": 111,
        "description": "тест",
    }
    transaction = Transaction(**data)
    expected_str = "id: 1\nДата: 2024-05-05\nКатегория: доход\nСумма: 111\nОписание: тест\n"
    assert str(transaction) == expected_str


def test_transaction_to_dict():
    data = {
        "id": 1,
        "date": date(2024, 5, 5),
        "category": "доход",
        "amount": 111,
        "description": "тест",
    }
    transaction = Transaction(**data)

    expected_dict = {
        "id": 1,
        "date": date(2024, 5, 5),
        "category": "доход",
        "amount": 111,
        "description": "тест"
    }
    assert type(transaction.to_dict) != dict
    assert transaction.to_dict() == expected_dict


def test_transaction_from_dict():
    data = {
        "id": 1,
        "date": date(2024, 5, 5),
        "category": "доход",
        "amount": 111,
        "description": "тест",
    }
    transaction = Transaction.from_dict(data)

    expected_dict = {
        "id": 1,
        "date": date(2024, 5, 5),
        "category": "доход",
        "amount": 111,
        "description": "тест"
    }
    
    assert transaction.id == expected_dict["id"]
    assert transaction.date == expected_dict["date"]
    assert transaction.category == expected_dict["category"]
    assert transaction.amount == expected_dict["amount"]
    assert transaction.description == expected_dict["description"]

