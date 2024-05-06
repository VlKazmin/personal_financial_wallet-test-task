import os
import pytest
import shutil

from .conftest import Capturing

from src.transactions.transaction_manager import TransactionManager


test_db_path = "data/test_database.json"
copy_test_db_path = "data/copy_test_database.json"


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    # делаем копию базы
    shutil.copy(test_db_path, copy_test_db_path)
    yield # тесты
    # удаляем временную копию
    os.remove(copy_test_db_path) 


@pytest.fixture
def manager():
    return TransactionManager(copy_test_db_path)


def test_check_transactions(manager):
    true_id = manager.check_transactions(1)
    assert true_id == True
    assert true_id != False

    false_id = manager.check_transactions(10)
    assert false_id == False
    assert false_id != True

    with Capturing() as get_message_output:
        manager.check_transactions(1, show=True)

    expected_output = [
        "",
        "id: 1",
        "Дата: 2024-05-01",
        "Категория: доход",
        "Сумма: 600",
        "Описание: Зарплата",
        "",
    ]

    assert expected_output == get_message_output


def test_add_transaction(manager):

    data = manager.file_manager.read_from_file()
    input_data = [
        "2024-05-01",
        "доход",
        600,
        "Зарплата",
    ]

    with Capturing() as get_message_output:
        manager.add_transaction(*input_data)

    expected_output = ["", "Запись успешно добавлена.", ""]
    assert expected_output == get_message_output

    new_data = manager.file_manager.read_from_file()
    assert len(data) != len(new_data)


def test_delete_transaction(manager):

    with Capturing() as get_message_output:
        manager.delete_transaction(4)

    expected_output = ["", "Запись с ID 4 успешно удалена.", ""]
    assert expected_output == get_message_output

    with Capturing() as get_message_output:
        manager.delete_transaction(999)

    expected_output = ["", "Запись с ID 999 не найдена.", ""]
    assert expected_output == get_message_output

    data = manager.file_manager.read_from_file()
    assert len(data) == 3


def test_edit_transaction(manager):
    # Считываем файл
    data = manager.file_manager.read_from_file()
    # Входные данные для записи id=3
    input_data = [3, None, "расход", None, None]
    # меняем "доход" на "расход"
    manager.edit_transaction(*input_data)

    # получаем обновленные данные
    new_data = manager.file_manager.read_from_file()
    assert data[2]["category"] != new_data[2]["category"]

    with Capturing() as get_message_output:
        manager.edit_transaction(999)

    expected_output = ["", "Запись с ID 999 не найдена.", ""]
    assert expected_output == get_message_output


def test_search_transactions(manager):
    # в тестовой базе 1 доходная операция
    with Capturing() as get_message_output:
        manager.search_transactions("доход")

    expected_output = [
        "",
        "Результаты поиска:",
        "",
        "id: 1",
        "Дата: 2024-05-01",
        "Категория: доход",
        "Сумма: 600",
        "Описание: Зарплата",
        "",
    ]
    assert get_message_output == expected_output
