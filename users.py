"""Функции для работы с пользователями."""


def add_user(users: list[dict], name: str, email: str) -> dict:
    """Добавить пользователя и вернуть его данные."""
    next_id = max((user["id"] for user in users), default=0) + 1
    user = {"id": next_id, "name": name, "email": email}
    users.append(user)
    return user


def find_user(users: list[dict], query: str) -> list[dict]:
    """Найти пользователей по имени или электронной почте."""
    query = query.lower()
    return [
        user
        for user in users
        if query in user["name"].lower() or query in user["email"].lower()
    ]


def get_user_by_id(users: list[dict], user_id: int) -> dict | None:
    """Найти пользователя по идентификатору."""
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def show_users(users: list[dict]) -> None:
    """Вывести список пользователей."""
    if not users:
        print("Пользователей пока нет.")
        return

    print("\n--- Пользователи ---")
    for user in users:
        print(f"ID: {user['id']} | {user['name']} | {user['email']}")
