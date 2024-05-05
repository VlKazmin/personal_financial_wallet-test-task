from dataclasses import dataclass
from datetime import date
from typing import Any, Dict


@dataclass
class Transaction:
    """
    Класс для представления транзакции.

    Attributes:
        id (int): Идентификатор транзакции.
        date (date): Дата транзакции.
        category (str): Категория транзакции (доход или расход).
        amount (float): Сумма транзакции.
        description (str): Описание транзакции.
    """

    id: int
    date: date
    category: str
    amount: float
    description: str

    def __str__(self) -> str:
        """
        Возвращает строковое представление транзакции.

        Returns:
            str: Строковое представление транзакции.
        """
        return (
            f"id: {self.id}\n"
            f"Дата: {self.date}\n"
            f"Категория: {self.category}\n"
            f"Сумма: {self.amount}\n"
            f"Описание: {self.description}\n"
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразует транзакцию в словарь.

        Returns:
            dict: Словарь с данными о транзакции.
        """
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Transaction":
        """
        Создает объект класса Transaction из словаря.

        Args:
            data (dict): Словарь с данными о транзакции.

        Returns:
            Transaction: Объект транзакции (Transaction.__str__()).
        """
        return cls(
            id=data["id"],
            date=data["date"],
            category=data["category"],
            amount=data["amount"],
            description=data["description"],
        )
