"""Модель статуса жалобы."""


class Status:
    """Статус обработки жалобы."""

    def __init__(self, status_id: int, name: str) -> None:
        """Создать статус."""
        self.id = status_id
        self.name = name

    @classmethod
    def from_data(cls, data: dict) -> "Status":
        """Создать статус из словаря JSON."""
        return cls(
            status_id=data["id"],
            name=data["name"],
        )

    def __str__(self) -> str:
        """Вернуть строковое представление статуса."""
        return self.name
