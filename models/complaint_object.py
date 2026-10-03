"""Модель объекта, на который подается жалоба."""


class ComplaintObject:
    """Объект предметной области, на который подается жалоба."""

    def __init__(
        self,
        object_id: int,
        name: str,
        description: str,
    ) -> None:
        """Создать объект жалобы."""
        self.id = object_id
        self.name = name
        self.description = description

    @classmethod
    def from_data(cls, data: dict) -> "ComplaintObject":
        """Создать объект из словаря JSON."""
        return cls(
            object_id=data["id"],
            name=data["name"],
            description=data["description"],
        )

    def __str__(self) -> str:
        """Вернуть строковое представление объекта."""
        return f"{self.id}: {self.name}"
