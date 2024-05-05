import json
from dataclasses import dataclass
from typing import Any, List


@dataclass
class FileManager:
    """
    Управление чтением и записью данных в файл.

    Attributes:
        filename (str): Путь к файлу, с которым ведется работа.
    """

    filename: str

    def read_from_file(self) -> List[dict]:
        """
        Считывает данные из файла и возвращает их в виде списка.

        Returns:
            List[Any]: Содержимое файла в виде списка.
        """
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def write_to_file(self, data: List[Any]) -> None:
        """
        Записывает данные в файл.

        Args:
            data (List[Any]): Список данных для записи в файл.
        """
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
