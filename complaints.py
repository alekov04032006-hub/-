"""Функции работы с коллекцией объектов Complaint."""

from datetime import datetime

from models.complaint import Complaint
from models.complaint_object import ComplaintObject
from models.status import Status
from models.user import User


def create_complaint(
    complaints: list[Complaint],
    user: User,
    complaint_object: ComplaintObject,
    status: Status,
    description: str,
) -> Complaint:
    """Создать жалобу и добавить ее в коллекцию."""
    next_id = max((item.id for item in complaints), default=0) + 1
    complaint = Complaint(
        complaint_id=next_id,
        user=user,
        complaint_object=complaint_object,
        status=status,
        description=description.strip(),
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    complaints.append(complaint)
    return complaint


def find_complaint(
    complaints: list[Complaint],
    query: str,
) -> list[Complaint]:
    """Найти жалобы по тексту описания."""
    query = query.lower()
    return [
        complaint
        for complaint in complaints
        if query in complaint.description.lower()
    ]


def find_complaints_by_user(
    complaints: list[Complaint],
    user_id: int,
) -> list[Complaint]:
    """Найти жалобы конкретного пользователя."""
    return [
        complaint
        for complaint in complaints
        if complaint.user.id == user_id
    ]


def find_complaints_by_status(
    complaints: list[Complaint],
    status_id: int,
) -> list[Complaint]:
    """Найти жалобы по идентификатору статуса."""
    return [
        complaint
        for complaint in complaints
        if complaint.status.id == status_id
    ]


def get_complaint_by_id(
    complaints: list[Complaint],
    complaint_id: int,
) -> Complaint | None:
    """Найти жалобу по идентификатору."""
    return next(
        (
            complaint for complaint in complaints
            if complaint.id == complaint_id
        ),
        None,
    )


def change_status(
    complaints: list[Complaint],
    complaint_id: int,
    status: Status,
) -> bool:
    """Изменить статус жалобы через метод объекта."""
    complaint = get_complaint_by_id(complaints, complaint_id)
    if complaint is None:
        return False
    complaint.change_status(status)
    return True


def sort_complaints(complaints: list[Complaint]) -> list[Complaint]:
    """Вернуть жалобы, отсортированные по дате."""
    return sorted(complaints, key=lambda complaint: complaint.created_at)


def complaint_statistics(complaints: list[Complaint]) -> dict[str, int]:
    """Посчитать количество жалоб по статусам."""
    statistics: dict[str, int] = {}
    for complaint in complaints:
        name = complaint.status.name
        statistics[name] = statistics.get(name, 0) + 1
    return statistics


def show_complaints(complaints: list[Complaint]) -> None:
    """Вывести список жалоб."""
    if not complaints:
        print("Жалоб пока нет.")
        return
    print("\n--- Жалобы ---")
    for complaint in complaints:
        print(complaint)
        print("-" * 70)
