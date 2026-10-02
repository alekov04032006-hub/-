"""Точка входа в систему учета жалоб пользователей."""

from complaints import (
    change_status,
    complaint_statistics,
    create_complaint,
    find_complaint,
    find_complaints_by_status,
    find_complaints_by_user,
    format_complaint,
    get_complaint_by_id,
    show_complaints,
)
from objects import (
    add_object,
    find_object,
    get_object_by_id,
    show_objects,
)
from statuses import STATUSES
from storage import load_json, save_json
from users import add_user, find_user, get_user_by_id, show_users
from utils import choose_status, input_int, input_non_empty

DATA_DIR = "data"
USERS_FILE = f"{DATA_DIR}/users.json"
OBJECTS_FILE = f"{DATA_DIR}/objects.json"
COMPLAINTS_FILE = f"{DATA_DIR}/complaints.json"


def show_search_results(
    complaints: list[dict],
    users: list[dict],
    objects: list[dict],
) -> None:
    """Вывести найденные жалобы или сообщение об отсутствии результатов."""
    if not complaints:
        print("Ничего не найдено.")
        return
    for complaint in complaints:
        print(format_complaint(complaint, users, objects))
        print("-" * 70)


def main() -> None:
    """Запустить главное меню программы."""
    users = load_json(USERS_FILE, [])
    objects = load_json(OBJECTS_FILE, [])
    complaints = load_json(COMPLAINTS_FILE, [])

    while True:
        print("\n=== Система учета жалоб пользователей ===")
        print("1. Показать пользователей")
        print("2. Добавить пользователя")
        print("3. Найти пользователя")
        print("4. Показать объекты")
        print("5. Добавить объект")
        print("6. Найти объект")
        print("7. Показать жалобы")
        print("8. Создать жалобу")
        print("9. Найти жалобу по описанию")
        print("10. Найти жалобы пользователя")
        print("11. Найти жалобы по статусу")
        print("12. Изменить статус жалобы")
        print("13. Сортировать жалобы")
        print("14. Статистика жалоб")
        print("0. Выход")

        choice = input_int("\nВыберите действие: ")

        if choice == 0:
            save_json(USERS_FILE, users)
            save_json(OBJECTS_FILE, objects)
            save_json(COMPLAINTS_FILE, complaints)
            print("Данные сохранены. Программа завершена.")
            break

        if choice == 1:
            show_users(users)

        elif choice == 2:
            name = input_non_empty("Введите имя пользователя: ")
            email = input_non_empty("Введите email: ")
            user = add_user(users, name, email)
            print(f"Пользователь добавлен. ID: {user['id']}")

        elif choice == 3:
            query = input_non_empty("Введите имя или email: ")
            results = find_user(users, query)
            if results:
                for user in results:
                    print(f"{user['id']}: {user['name']} | {user['email']}")
            else:
                print("Пользователь не найден.")

        elif choice == 4:
            show_objects(objects)

        elif choice == 5:
            name = input_non_empty("Введите название объекта: ")
            description = input_non_empty("Введите описание объекта: ")
            item = add_object(objects, name, description)
            print(f"Объект добавлен. ID: {item['id']}")

        elif choice == 6:
            query = input_non_empty("Введите название объекта: ")
            results = find_object(objects, query)
            if results:
                for item in results:
                    print(
                        f"{item['id']}: {item['name']} | "
                        f"{item['description']}"
                    )
            else:
                print("Объект не найден.")

        elif choice == 7:
            show_complaints(complaints, users, objects)

        elif choice == 8:
            show_users(users)
            user_id = input_int("Введите ID пользователя: ")
            if not get_user_by_id(users, user_id):
                print("Ошибка: пользователь не найден.")
                continue

            show_objects(objects)
            object_id = input_int("Введите ID объекта: ")
            if not get_object_by_id(objects, object_id):
                print("Ошибка: объект не найден.")
                continue

            description = input_non_empty("Введите описание проблемы: ")
            complaint = create_complaint(
                complaints,
                user_id,
                object_id,
                description,
            )
            if complaint is None:
                print("Ошибка: некорректные данные жалобы.")
            else:
                print("\nЖалоба создана:")
                print(format_complaint(complaint, users, objects))

        elif choice == 9:
            query = input_non_empty("Введите текст для поиска: ")
            results = find_complaint(complaints, query)
            show_search_results(results, users, objects)

        elif choice == 10:
            user_id = input_int("Введите ID пользователя: ")
            results = find_complaints_by_user(complaints, user_id)
            show_search_results(results, users, objects)

        elif choice == 11:
            status = choose_status(STATUSES)
            results = find_complaints_by_status(complaints, status)
            show_search_results(results, users, objects)

        elif choice == 12:
            complaint_id = input_int("Введите ID жалобы: ")
            if not get_complaint_by_id(complaints, complaint_id):
                print("Жалоба не найдена.")
                continue

            status = choose_status(STATUSES)
            if change_status(complaints, complaint_id, status):
                print("Статус жалобы изменен.")

        elif choice == 13:
            sorted_complaints = sorted(
                complaints,
                key=lambda item: item["created_at"],
            )
            show_search_results(sorted_complaints, users, objects)

        elif choice == 14:
            statistics = complaint_statistics(complaints)
            print("\n--- Статистика ---")
            print(f"Всего жалоб: {len(complaints)}")
            for status, count in statistics.items():
                print(f"{status}: {count}")

        else:
            print("Ошибка: неизвестный пункт меню.")


if __name__ == "__main__":
    main()
