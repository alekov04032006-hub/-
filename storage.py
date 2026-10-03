"""Загрузка и сохранение объектов в JSON."""

import json

from models import Complaint, ComplaintObject, Status, User


def _load_raw(filename: str, default: list[dict]) -> list[dict]:
    """Загрузить список словарей из JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except FileNotFoundError:
        return default.copy()
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} содержит некорректный JSON.")
    except OSError as error:
        print(f"Ошибка чтения файла: {error}")
    return default.copy()


def load_users(filename: str) -> list[User]:
    """Загрузить пользователей и создать объекты User."""
    return [User.from_data(data) for data in _load_raw(filename, [])]


def save_users(filename: str, users: list[User]) -> None:
    """Сохранить объекты User в JSON."""
    data = [
        {"id": user.id, "name": user.name, "email": user.email}
        for user in users
    ]
    _save_raw(filename, data)


def load_objects(filename: str) -> list[ComplaintObject]:
    """Загрузить объекты жалоб и создать объекты ComplaintObject."""
    return [
        ComplaintObject.from_data(data)
        for data in _load_raw(filename, [])
    ]


def save_objects(
    filename: str,
    objects: list[ComplaintObject],
) -> None:
    """Сохранить объекты ComplaintObject в JSON."""
    data = [
        {
            "id": item.id,
            "name": item.name,
            "description": item.description,
        }
        for item in objects
    ]
    _save_raw(filename, data)


def load_statuses(filename: str) -> list[Status]:
    """Загрузить статусы и создать объекты Status."""
    return [Status.from_data(data) for data in _load_raw(filename, [])]


def save_statuses(filename: str, statuses: list[Status]) -> None:
    """Сохранить объекты Status в JSON."""
    data = [
        {"id": status.id, "name": status.name}
        for status in statuses
    ]
    _save_raw(filename, data)


def load_complaints(
    filename: str,
    users: list[User],
    objects: list[ComplaintObject],
    statuses: list[Status],
) -> list[Complaint]:
    """Загрузить жалобы и восстановить связи между объектами."""
    result: list[Complaint] = []
    for data in _load_raw(filename, []):
        user = next(
            (item for item in users if item.id == data["user_id"]),
            None,
        )
        complaint_object = next(
            (item for item in objects if item.id == data["object_id"]),
            None,
        )
        status = next(
            (item for item in statuses if item.id == data["status_id"]),
            None,
        )
        if user is None or complaint_object is None or status is None:
            continue
        result.append(
            Complaint(
                complaint_id=data["id"],
                user=user,
                complaint_object=complaint_object,
                status=status,
                description=data["description"],
                created_at=data["created_at"],
            )
        )
    return result


def save_complaints(filename: str, complaints: list[Complaint]) -> None:
    """Сохранить объекты Complaint в JSON по идентификаторам связей."""
    data = [
        {
            "id": complaint.id,
            "user_id": complaint.user.id,
            "object_id": complaint.object.id,
            "status_id": complaint.status.id,
            "description": complaint.description,
            "created_at": complaint.created_at,
        }
        for complaint in complaints
    ]
    _save_raw(filename, data)


def _save_raw(filename: str, data: list[dict]) -> None:
    """Записать список словарей в JSON."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Ошибка сохранения файла: {error}")
