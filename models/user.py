"""Модель пользователя системы."""


class User:
    """Пользователь системы."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        """Создать пользователя."""
        self.id = user_id
        self.name = name
        self.email = email

    @classmethod
    def from_data(cls, data: dict) -> "User":
        """Создать пользователя из словаря JSON."""
        return cls(
            user_id=data["id"],
            name=data["name"],
            email=data["email"],
        )

    def __str__(self) -> str:
        """Вернуть строковое представление пользователя."""
        return f"{self.id}: {self.name} ({self.email})"
