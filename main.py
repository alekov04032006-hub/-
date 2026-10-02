from datetime import datetime


def create_complaint(user_name, object_name, description):
    """Создает новую жалобу пользователя."""
    complaint = {
        "user": user_name,
        "object": object_name,
        "description": description,
        "status": "Новая",
        "created_at": datetime.now()
    }

    return complaint


def validate_complaint(user_name, object_name, description):
    """Проверяет корректность данных жалобы."""
    if not user_name:
        return False

    if not object_name:
        return False

    if not description:
        return False

    return True


def get_complaint_status(complaint):
    """Возвращает текущий статус жалобы."""
    return complaint["status"]


def print_complaint(complaint):
    """Выводит информацию о жалобе."""
    print("\n--- Информация о жалобе ---")
    print(f"Пользователь: {complaint['user']}")
    print(f"Объект: {complaint['object']}")
    print(f"Описание: {complaint['description']}")
    print(f"Статус: {complaint['status']}")
    print(
        f"Дата создания: "
        f"{complaint['created_at'].strftime('%d.%m.%Y %H:%M')}"
    )


def main():
    print("=== Система учета жалоб пользователей ===")

    user_name = input("Введите имя пользователя: ").strip()
    object_name = input("Введите объект жалобы: ").strip()
    description = input("Введите описание проблемы: ").strip()

    if not validate_complaint(user_name, object_name, description):
        print("\nОшибка: необходимо заполнить все поля.")
        return

    complaint = create_complaint(
        user_name,
        object_name,
        description
    )

    print_complaint(complaint)

    status = get_complaint_status(complaint)
    print(f"\nТекущий статус обращения: {status}")


if __name__ == "__main__":
    main()