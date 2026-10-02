"""Работа с JSON-файлами."""

import json


def load_json(filename: str, default: list) -> list:
    """Загрузить список данных из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return default.copy()
    except FileNotFoundError:
        return default.copy()
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} содержит некорректный JSON.")
        return default.copy()
    except OSError as error:
        print(f"Ошибка чтения файла: {error}")
        return default.copy()


def save_json(filename: str, data: list) -> None:
    """Сохранить список данных в JSON-файл."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Ошибка сохранения файла: {error}")
