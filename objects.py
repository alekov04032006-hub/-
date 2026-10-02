"""Функции для работы с объектами жалоб."""


def add_object(
    objects: list[dict],
    name: str,
    description: str,
) -> dict:
    """Добавить объект и вернуть его данные."""
    next_id = max((item["id"] for item in objects), default=0) + 1
    item = {
        "id": next_id,
        "name": name,
        "description": description,
    }
    objects.append(item)
    return item


def find_object(objects: list[dict], query: str) -> list[dict]:
    """Найти объекты по названию."""
    query = query.lower()
    return [
        item for item in objects if query in item["name"].lower()
    ]


def get_object_by_id(objects: list[dict], object_id: int) -> dict | None:
    """Найти объект по идентификатору."""
    for item in objects:
        if item["id"] == object_id:
            return item
    return None


def show_objects(objects: list[dict]) -> None:
    """Вывести список объектов."""
    if not objects:
        print("Объектов пока нет.")
        return

    print("\n--- Объекты ---")
    for item in objects:
        print(
            f"ID: {item['id']} | {item['name']} | "
            f"{item['description']}"
        )
