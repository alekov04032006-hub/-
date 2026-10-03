"""Вспомогательные функции интерфейса."""

from models.status import Status


def input_int(prompt: str) -> int:
    """Запросить целое число и повторять ввод при ошибке."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: необходимо ввести целое число.")


def input_non_empty(prompt: str) -> str:
    """Запросить непустую строку."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: поле не должно быть пустым.")


def choose_status(statuses: list[Status]) -> Status:
    """Показать статусы и вернуть выбранный объект Status."""
    print("\nСтатусы:")
    for status in statuses:
        print(f"{status.id}. {status.name}")
    while True:
        choice = input_int("Выберите статус: ")
        status = next(
            (item for item in statuses if item.id == choice),
            None,
        )
        if status is not None:
            return status
        print("Ошибка: такого пункта нет.")
