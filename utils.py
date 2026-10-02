"""Вспомогательные функции для безопасного ввода."""


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


def choose_status(statuses: tuple[str, ...]) -> str:
    """Показать статусы и вернуть выбранный."""
    print("\nСтатусы:")
    for index, status in enumerate(statuses, start=1):
        print(f"{index}. {status}")

    while True:
        choice = input_int("Выберите статус: ")
        if 1 <= choice <= len(statuses):
            return statuses[choice - 1]
        print("Ошибка: такого пункта нет.")
