from src.transactions.transaction_manager import TransactionManager
from src.utils.validators import (
    get_description,
    get_valid_amount,
    get_valid_category,
    get_valid_date,
)
from src.balance.balance_manager import BalanceManager


PATH_TO_DATABASE = "data/transactions.json"

CHOICE_BALANCE_INFO = "1"
CHOICE_ADD_TRANSACTION = "2"
CHOICE_DELETE_TRANSACTION = "3"
CHOICE_EDIT_TRANSACTION = "4"
CHOICE_SEARCH_TRANSACTION = "5"
CHOICE_SHOW_ALL = "6"
CHOICE_EXIT = "7"


def balance_submenu(balance_manager: BalanceManager) -> None:
    """
    Подменю для управления балансом.

    Args:
        balance_manager (BalanceManager): Менеджер баланса.
    """

    BALANCE = "1"
    INCOME = "2"
    EXPENSE = "3"
    BACK = "4"

    while True:
        print("1. Вывести баланс")
        print("2. Все доходные записи")
        print("3. Все расходные записи")
        print("4. Назад")
        print()

        sub_choice: str = input("Выберите действие: ")
        try:
            if sub_choice == BALANCE:
                balance_manager.current_balance()
            elif sub_choice == INCOME:
                balance_manager.current_balance(show_income=True)
            elif sub_choice == EXPENSE:
                balance_manager.current_balance(show_expense=True)
            elif sub_choice == BACK:
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")

        except Exception as e:
            print(f"Ошибка: {e}")
            continue


def add_transactions_submenu(transaction_manager: TransactionManager) -> None:
    """
    Подменю для добавления транзакций.

    Args:
        transaction_manager (TransactionManager): Менеджер транзакций.
    """

    ADD_TRANSACTION = "1"
    BACK = "2"

    while True:
        print("1. Добавить транзакцию")
        print("2. Назад")
        print()

        sub_choice: str = input("Выберите действие: ")

        if sub_choice == ADD_TRANSACTION:

            date: str = get_valid_date("Введите дату (гггг-мм-дд): ")
            category: str = get_valid_category(
                "Введите категорию ",
                " (доход/расход): ",
            )
            amount: float = get_valid_amount("Введите сумму: ")
            description: str = get_description("Введите описание: ")

            transaction_manager.add_transaction(date, category, amount, description)
            print("Транзакция успешно добавлена.")
            break

        if sub_choice == BACK:
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


def delete_transactions_submenu(transaction_manager: TransactionManager) -> None:
    """
    Подменю для удаления транзакций.

    Args:
        transaction_manager (TransactionManager): Менеджер транзакций.
    """

    DEL_TRANSACTION = "1"
    BACK = "2"

    while True:
        print("1. Удалить транзакцию")
        print("2. Назад")
        print()

        sub_choice: str = input("Выберите действие: ")
        print()

        if sub_choice == DEL_TRANSACTION:
            while True:
                transaction_id: str = input("Введите ID транзакции для удаления: ")
                try:
                    transaction_id: int = int(transaction_id)
                    transaction_manager.delete_transaction(
                        transaction_id,
                    )
                    break
                except ValueError:
                    print("ID транзакции должен быть целым числом")
        elif sub_choice == BACK:
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


def edit_transactions_submenu(transaction_manager: TransactionManager) -> None:
    """
    Подменю для редактирования транзакций.

    Args:
        transaction_manager (TransactionManager): Менеджер транзакций.
    """
    EDIT_TRANSACTION = "1"
    BACK = "2"

    while True:
        print("1. Редактировать транзакцию")
        print("2. Назад")
        print()

        sub_choice: str = input("Выберите действие: ")

        if sub_choice == EDIT_TRANSACTION:
            while True:
                transaction_id: str = input(
                    "Введите ID транзакции для редактирования: "
                )
                try:
                    transaction_id: int = int(transaction_id)
                    if transaction_manager.check_transactions(
                        transaction_id,
                        show=True,
                    ):
                        date: str = get_valid_date(
                            "Введите новую дату (гггг-мм-дд), оставьте"
                            " пустым, если не хотите изменять: ",
                            skip_allowed=True,
                        )

                        category: str = get_valid_category(
                            "Введите новую категорию (доход/расход), "
                            "оставьте пустым, "
                            "если не хотите изменять:",
                            skip_allowed=True,
                        )
                        amount: float = get_valid_amount(
                            "Введите новую сумму, оставьте пустым, "
                            "если не хотите изменять: ",
                            skip_allowed=True,
                        )
                        description: str = get_description(
                            "Введите новое описание, оставьте пустым,"
                            " если не хотите изменять: ",
                            skip_allowed=True,
                        )

                except (TypeError, ValueError):
                    print("ID транзакции должен быть целым числом")

                transaction_manager.edit_transaction(
                    transaction_id,
                    date if date else None,
                    category if category else None,
                    amount if amount else None,
                    description if description else None,
                )
                break

        elif sub_choice == BACK:
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
            print()


def search_transactions_submenu(transaction_manager: TransactionManager) -> None:
    """
    Подменю для поиска транзакций.

    Args:
        transaction_manager (TransactionManager): Менеджер транзакций.
    """
    FIND_TRANSACTION = "1"
    BACK = "2"

    while True:
        print("1. Найти транзакцию")
        print("2. Назад")
        print()

        sub_choice: str = input("Выберите действие: ")

        if sub_choice == FIND_TRANSACTION:
            while True:
                category: str = get_valid_category(
                    "Введите категорию для поиска(доход/расход): ",
                    skip_allowed=True,
                )
                date: str = get_valid_date(
                    "Введите дату для поиска (гггг-мм-дд): ",
                    skip_allowed=True,
                )
                amount: float = get_valid_amount(
                    "Введите сумму для поиска: ",
                    skip_allowed=True,
                )

                transaction_manager.search_transactions(
                    category if category else None,
                    date if date else None,
                    amount if amount else None,
                )
                break
        elif sub_choice == BACK:
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


def main():
    transaction_manager = TransactionManager(PATH_TO_DATABASE)
    balance_manager = BalanceManager(PATH_TO_DATABASE)

    while True:
        print("1. Информация о балансе")
        print("2. Добавить транзакцию")
        print("3. Удалить транзакцию")
        print("4. Редактировать транзакцию")
        print("5. Поиск транзакции")
        print("6. Показать все записи")
        print("7. Выйти")
        print()

        choice = input("Выберите действие: ")

        if choice == CHOICE_BALANCE_INFO:
            balance_submenu(balance_manager)

        elif choice == CHOICE_ADD_TRANSACTION:
            add_transactions_submenu(transaction_manager)

        elif choice == CHOICE_DELETE_TRANSACTION:
            delete_transactions_submenu(transaction_manager)

        elif choice == CHOICE_EDIT_TRANSACTION:
            edit_transactions_submenu(transaction_manager)

        elif choice == CHOICE_SEARCH_TRANSACTION:
            search_transactions_submenu(transaction_manager)

        elif choice == CHOICE_SHOW_ALL:
            transaction_manager.show_all()

        elif choice == CHOICE_EXIT:
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
