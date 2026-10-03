"""Функции работы со статусами жалоб."""

from models.status import Status

DEFAULT_STATUSES = (
    "Новая",
    "На рассмотрении",
    "Решена",
    "Отклонена",
)


def create_default_statuses() -> list[Status]:
    """Создать стандартный набор статусов."""
    return [
        Status(status_id=index, name=name)
        for index, name in enumerate(DEFAULT_STATUSES, start=1)
    ]


def get_status_by_id(
    statuses: list[Status],
    status_id: int,
) -> Status | None:
    """Найти статус по идентификатору."""
    return next(
        (status for status in statuses if status.id == status_id),
        None,
    )


def get_status_by_name(
    statuses: list[Status],
    name: str,
) -> Status | None:
    """Найти статус по названию."""
    return next((status for status in statuses if status.name == name), None)


def show_statuses(statuses: list[Status]) -> None:
    """Вывести доступные статусы."""
    print("\n--- Статусы ---")
    for status in statuses:
        print(f"{status.id}. {status.name}")
