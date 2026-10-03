"""Функции работы с коллекцией пользователей."""

from models.user import User


def add_user(users: list[User], name: str, email: str) -> User:
    """Создать пользователя и добавить его в коллекцию."""
    next_id = max((user.id for user in users), default=0) + 1
    user = User(next_id, name, email)
    users.append(user)
    return user


def find_user(users: list[User], query: str) -> list[User]:
    """Найти пользователей по имени или email."""
    query = query.lower()
    return [
        user
        for user in users
        if query in user.name.lower() or query in user.email.lower()
    ]


def get_user_by_id(users: list[User], user_id: int) -> User | None:
    """Найти пользователя по идентификатору."""
    return next((user for user in users if user.id == user_id), None)


def show_users(users: list[User]) -> None:
    """Вывести пользователей."""
    if not users:
        print("Пользователей пока нет.")
        return
    print("\n--- Пользователи ---")
    for user in users:
        print(user)
