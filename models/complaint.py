"""Модель жалобы и ее поведение."""

from .complaint_object import ComplaintObject
from .status import Status
from .user import User


class Complaint:
    """Жалоба пользователя на объект системы."""

    def __init__(
        self,
        complaint_id: int,
        user: User,
        complaint_object: ComplaintObject,
        status: Status,
        description: str,
        created_at: str,
    ) -> None:
        """Создать жалобу."""
        self.id = complaint_id
        self.user = user
        self.object = complaint_object
        self.status = status
        self.description = description
        self.created_at = created_at

    def change_status(self, status: Status) -> None:
        """Изменить статус жалобы."""
        self.status = status

    def __str__(self) -> str:
        """Вернуть строковое представление жалобы."""
        return (
            f"ID: {self.id} | Пользователь: {self.user.name} | "
            f"Объект: {self.object.name} | Статус: {self.status.name}\n"
            f"Описание: {self.description} | Дата: {self.created_at}"
        )
