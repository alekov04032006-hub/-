"""Функции работы с коллекцией объектов жалоб."""

from models.complaint_object import ComplaintObject


def add_object(
    objects: list[ComplaintObject],
    name: str,
    description: str,
) -> ComplaintObject:
    """Создать объект и добавить его в коллекцию."""
    next_id = max((item.id for item in objects), default=0) + 1
    item = ComplaintObject(next_id, name, description)
    objects.append(item)
    return item


def find_object(
    objects: list[ComplaintObject],
    query: str,
) -> list[ComplaintObject]:
    """Найти объекты по названию."""
    query = query.lower()
    return [item for item in objects if query in item.name.lower()]


def get_object_by_id(
    objects: list[ComplaintObject],
    object_id: int,
) -> ComplaintObject | None:
    """Найти объект по идентификатору."""
    return next((item for item in objects if item.id == object_id), None)


def show_objects(objects: list[ComplaintObject]) -> None:
    """Вывести объекты."""
    if not objects:
        print("Объектов пока нет.")
        return
    print("\n--- Объекты ---")
    for item in objects:
        print(f"{item} | {item.description}")
