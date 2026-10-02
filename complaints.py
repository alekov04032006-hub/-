"""Функции для работы с жалобами."""

from datetime import datetime

from statuses import STATUSES


def validate_complaint(
    user_id: int,
    object_id: int,
    description: str,
) -> bool:
    """Проверить корректность данных жалобы."""
    return user_id > 0 and object_id > 0 and bool(description.strip())


def create_complaint(
    complaints: list[dict],
    user_id: int,
    object_id: int,
    description: str,
) -> dict | None:
    """Создать новую жалобу со статусом «Новая»."""
    if not validate_complaint(user_id, object_id, description):
        return None

    next_id = max((item["id"] for item in complaints), default=0) + 1
    complaint = {
        "id": next_id,
        "user_id": user_id,
        "object_id": object_id,
        "description": description.strip(),
        "status": STATUSES[0],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    complaints.append(complaint)
    return complaint


def get_complaint_status(complaint: dict) -> str:
    """Вернуть текущий статус жалобы."""
    return complaint["status"]


def find_complaint(
    complaints: list[dict],
    query: str,
) -> list[dict]:
    """Найти жалобы по описанию."""
    query = query.lower()
    return [
        item
        for item in complaints
        if query in item["description"].lower()
    ]


def find_complaints_by_user(
    complaints: list[dict],
    user_id: int,
) -> list[dict]:
    """Найти жалобы конкретного пользователя."""
    return [item for item in complaints if item["user_id"] == user_id]


def find_complaints_by_status(
    complaints: list[dict],
    status: str,
) -> list[dict]:
    """Найти жалобы с указанным статусом."""
    return [item for item in complaints if item["status"] == status]


def change_status(
    complaints: list[dict],
    complaint_id: int,
    new_status: str,
) -> bool:
    """Изменить статус жалобы."""
    if new_status not in STATUSES:
        return False

    for complaint in complaints:
        if complaint["id"] == complaint_id:
            complaint["status"] = new_status
            return True
    return False


def sort_complaints(complaints: list[dict]) -> list[dict]:
    """Вернуть жалобы, отсортированные по дате создания."""
    return sorted(
        complaints,
        key=lambda complaint: complaint["created_at"],
    )


def complaint_statistics(complaints: list[dict]) -> dict[str, int]:
    """Посчитать количество жалоб по статусам."""
    statistics = {status: 0 for status in STATUSES}
    for complaint in complaints:
        status = complaint["status"]
        statistics[status] = statistics.get(status, 0) + 1
    return statistics


def get_complaint_by_id(
    complaints: list[dict],
    complaint_id: int,
) -> dict | None:
    """Найти жалобу по идентификатору."""
    for complaint in complaints:
        if complaint["id"] == complaint_id:
            return complaint
    return None


def format_complaint(
    complaint: dict,
    users: list[dict],
    objects: list[dict],
) -> str:
    """Сформировать строковое представление жалобы для вывода."""
    user_name = next(
        (
            user["name"]
            for user in users
            if user["id"] == complaint["user_id"]
        ),
        "Неизвестный пользователь",
    )
    object_name = next(
        (
            item["name"]
            for item in objects
            if item["id"] == complaint["object_id"]
        ),
        "Неизвестный объект",
    )
    return (
        f"ID: {complaint['id']} | Пользователь: {user_name} | "
        f"Объект: {object_name} | Статус: {complaint['status']}\n"
        f"Описание: {complaint['description']} | "
        f"Дата: {complaint['created_at']}"
    )


def show_complaints(
    complaints: list[dict],
    users: list[dict],
    objects: list[dict],
) -> None:
    """Вывести список жалоб."""
    if not complaints:
        print("Жалоб пока нет.")
        return

    print("\n--- Жалобы ---")
    for complaint in complaints:
        print(format_complaint(complaint, users, objects))
        print("-" * 70)
