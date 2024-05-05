from dataclasses import dataclass
from typing import Optional

from ..utils.file_manager import FileManager
from .transaction import Transaction, date


@dataclass
class TransactionManager:
    """Класс для работы с транзакциями"""

    filename: str

    def __post_init__(self):
        """
        Пост-инициализация объекта BalanceManager.

        Создает экземпляр FileManager для работы с файлом транзакций.
        """

        self.file_manager = FileManager(self.filename)

    def check_transactions(
        self,
        transaction_id: int,
        show: Optional[bool] = False,
    ) -> bool:
        """
        Проверка наличия конкретной записи в файле по id.

        Args:
            transaction_id (int): ID значение искомого объекта.
            show (bool, optional): Флаг для вывода информации
            о найденом объекте в виде словаря. По умолчанию False.

        Returns:
            bool: Если в БД есть записть, то возвращает
            True, инача False.
        """
        transactions = self.file_manager.read_from_file()

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                if show:
                    print()
                    print(Transaction.from_dict(transaction))
                return True
        return False

    def add_transaction(
        self,
        date: date,
        category: str,
        amount: float,
        description: str,
    ) -> None:
        """
        Записывает в файл БД информацию о новой транзакции.

        Args:
            date (date): Дата транзакции.
            category (str): Категория транзакции (доход или расход).
            amount (float): Сумма транзакции.
            description (str): Описание транзакции.
        """

        transactions = self.file_manager.read_from_file()
        new_id = transactions[-1]["id"] + 1 if transactions else 1
        amount = round(float(amount), 2) if isinstance(amount, float) else ""

        new_transaction = Transaction(
            id=new_id,
            date=date,
            category=category,
            amount=amount,
            description=description,
        )
        transactions.append(new_transaction.to_dict())
        self.file_manager.write_to_file(transactions)
        print()
        print("Запись успешно добавлена.")
        print()

    def delete_transaction(
        self,
        transaction_id: int,
    ) -> None:
        """
        Удаляет транзакцию по переданному номеру (ID).

        Args:
            transaction_id (int): ID транзакции которую необходимо удалить.
        """

        transactions = self.file_manager.read_from_file()
        found = False

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transactions.remove(transaction)
                found = True

        if not found:
            print()
            print(f"Запись с ID {transaction_id} не найдена.")
            print()
            return

        self.file_manager.write_to_file(transactions)
        print()
        print(f"Запись с ID {transaction_id} успешно удалена.")
        print()

    def edit_transaction(
        self,
        transaction_id: int,
        date: date = None,
        category: str = None,
        amount: float = None,
        description: str = None,
    ) -> None:
        """
        Вносит изменения в соотвествии с переданными аргументами
        в ранее созданную транзакцию.

        Args:
            transaction_id (int): ID номер транзакции.
            date (date, optional): Дата транзакции. По умолчанию None.
            category (str, optional): Категория транзакции (доход или расход).
            Defaults to None.
            amount (float, optional): Сумма транзакции. По умолчанию None.
            description (str, optional): Описание транзакции.
            По умолчанию None.
        """
        data = self.file_manager.read_from_file()
        found = False

        for transaction in data:
            if transaction["id"] == transaction_id:
                found = True
                if date is not None:
                    transaction["date"] = date
                if category is not None:
                    transaction["category"] = category
                if amount is not None:
                    transaction["amount"] = amount
                if description is not None:
                    transaction["description"] = description

                self.file_manager.write_to_file(data)
                print()
                print("Запись успешно отредактирована.")
                print(Transaction.from_dict(transaction))
                break

        if not found:
            print()
            print(f"Запись с ID {transaction_id} не найдена.")
            print()
            return

    def search_transactions(
        self,
        category: str = None,
        date: date = None,
        amount: float = None,
    ):
        """Поиск и вывод информации о транзакциях по заданным критериям.
        Исключает возможность поиска если не передано ни одного аргумента.

        Args:
            category (str, optional): Категория транзакции (доход или расход).
            По умолчанию None.
            date (date, optional): Дата транзакции. По умолчанию None.
            amount (float, optional): Сумма транзакции. По умолчанию None.
        """

        if category is None and date is None and amount is None:
            print()
            print(
                "Не указаны критерии поиска. ",
                "Укажите хотя бы один критерий поиска.",
            )
            print()
            return

        transactions = self.file_manager.read_from_file()
        filtered_transactions = []

        for transaction in transactions:
            if (
                (category is None or transaction["category"] == category)
                and (date is None or transaction["date"] == date)
                and (amount is None or transaction["amount"] == amount)
            ):
                filtered_transactions.append(Transaction.from_dict(transaction))

        if not filtered_transactions:
            print()
            print("По заданному критерию поиска результаты не обнаружены.")
            print()

        else:
            print()
            print("Результаты поиска:")
            print()
            for transaction in filtered_transactions:
                print(transaction)

    def show_all(self):
        """Выводит все существующие транзакции."""

        try:
            transactions = self.file_manager.read_from_file()
            results = []

            for transaction in transactions:
                results.append(Transaction.from_dict(transaction))
            for result in results:
                print(result)
        except ValueError:
            pass
