from dataclasses import dataclass
from typing import Optional

from ..utils.file_manager import FileManager


@dataclass
class BalanceManager:
    """
    Управление балансом на основе транзакций.

    Args:
        filename (str): Имя файла, в котором хранятся транзакции.
    """

    filename: str

    def __post_init__(self):
        """
        Пост-инициализация объекта BalanceManager.

        Создает экземпляр FileManager для работы с файлом транзакций.
        """
        self.file_manager = FileManager(self.filename)

    def _calculate(self, category: str) -> float:
        """
        Расчёт суммы транзакций в зависимости от выбранной категории

        Args:
            category (str): Категория транзакций (доход или расход)

        Returns:
            float: Сумма всех операций выбранной категории.
        """

        transactions = self.file_manager.read_from_file()

        return sum(
            transaction["amount"]
            for transaction in transactions
            if transaction["category"] == category
        )

    def current_balance(
        self,
        show_income: Optional[bool] = False,
        show_expense: Optional[bool] = False,
    ) -> None:
        """
        Вывод текущего баланса или суммы доходов/расходов
        в зависимости от переданных параметров.

        Args:
            show_income (bool, optional): Флаг для вывода суммы доходов.
            По умолчанию False.
            show_expense (bool, optional): Флаг для вывода суммы расходов.
            По умолчанию False.

        Raises:
            ValueError: Вызывается, если оба флага show_income и show_expense
            установлены в True.
        """
        if show_income is True and show_expense is True:
            raise ValueError(
                "Нельзя указать одновременно два аргумента",
                " как False.",
            )

        total_income = self._calculate("доход")
        total_expense = self._calculate("расход")

        if show_income or show_expense:
            if show_income:
                print(f"Доходы: {total_income}")
                print()
            if show_expense:
                print(f"Расходы: {total_expense}")
                print()
        else:
            balance = total_income - total_expense
            print(f"Текущий баланс: {balance}")
            print()
