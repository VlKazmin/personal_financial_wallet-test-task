from datetime import datetime


def get_valid_date(msg: str = None, skip_allowed: bool = False):
    """
    Получает от пользователя дату в формате гггг-мм-дд.

    Args:
        msg (str, optional): Сообщение пользователю.
        skip_allowed (bool, optional): Позволяет пропустить ввод данных,
        если установлено значение True. По умолчанию False.

    Returns:
        str: Строка с датой в формате гггг-мм-дд или None,
        если ввод был пропущен и skip_allowed установлено в True.
    """
    while True:
        date_str = input(msg)
        if skip_allowed and not date_str:
            return None
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return str(date)
        except ValueError:
            print("Некорректный формат даты.")


def get_valid_category(msg: str = None, skip_allowed: bool = False):
    """
    Получает от пользователя категорию транзакции (доход или расход).

    Args:
        msg (str, optional): Сообщение пользователю.
        skip_allowed (bool, optional): Позволяет пропустить ввод данных,
        если установлено значение True. По умолчанию False.

    Returns:
        str: Строка с категорией ("доход" или "расход") или None,
        если ввод был пропущен и skip_allowed установлено в True.
    """
    while True:
        category = input(msg).lower()
        if skip_allowed and not category:
            return None
        try:
            if category in ["доход", "расход"]:
                return category
            else:
                raise ValueError("Некорректная категория")
        except ValueError as e:
            print(e)


def get_valid_amount(msg: str = None, skip_allowed: bool = False):
    """
    Получает от пользователя сумму транзакции.

    Args:
        msg (str, optional): Сообщение пользователю.
        skip_allowed (bool, optional): Позволяет пропустить ввод данных,
        если установлено значение True. По умолчанию False.

    Returns:
        float: Сумма транзакции или None,
        если ввод был пропущен и skip_allowed
        установлено в True.
    """
    while True:
        amount_str = input(msg)
        if skip_allowed and not amount_str:
            return None
        try:
            amount = float(amount_str)
            return amount
        except ValueError:
            print("Сумма должна быть числом. Попробуйте снова.")


def get_description(msg: str = None, skip_allowed: bool = False):
    """
    Получает от пользователя описание транзакции.

    Args:
        msg (str, optional): Сообщение пользователю.
        skip_allowed (bool, optional): Позволяет пропустить ввод данных,
        если установлено значение True. По умолчанию False.

    Returns:
        str: Описание транзакции или None,
        если ввод был пропущен и skip_allowed
        установлено в True.
    """
    description = input(msg) if msg else input("Введите описание: ")
    if skip_allowed and not description:
        return None
    return description
