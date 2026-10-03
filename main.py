"""Точка входа в систему учета жалоб пользователей."""

from complaints import (
    change_status,
    complaint_statistics,
    create_complaint,
    find_complaint,
    find_complaints_by_status,
    find_complaints_by_user,
    get_complaint_by_id,
    show_complaints,
    sort_complaints,
)
from objects import (
    add_object,
    find_object,
    get_object_by_id,
    show_objects,
)
from statuses import create_default_statuses
from storage import (
    load_complaints,
    load_objects,
    load_statuses,
    load_users,
    save_complaints,
    save_objects,
    save_statuses,
    save_users,
)
from users import add_user, find_user, get_user_by_id, show_users
from utils import choose_status, input_int, input_non_empty

DATA_DIR = "data"
USERS_FILE = f"{DATA_DIR}/users.json"
OBJECTS_FILE = f"{DATA_DIR}/objects.json"
STATUSES_FILE = f"{DATA_DIR}/statuses.json"
COMPLAINTS_FILE = f"{DATA_DIR}/complaints.json"


def show_results(complaints: list) -> None:
    """Вывести найденные жалобы."""
    if not complaints:
        print("Ничего не найдено.")
        return
    for complaint in complaints:
        print(complaint)
        print("-" * 70)


def save_all(users, objects, statuses, complaints) -> None:
    """Сохранить все данные проекта."""
    save_users(USERS_FILE, users)
    save_objects(OBJECTS_FILE, objects)
    save_statuses(STATUSES_FILE, statuses)
    save_complaints(COMPLAINTS_FILE, complaints)


def main() -> None:
    """Запустить главное меню программы."""
    users = load_users(USERS_FILE)
    objects = load_objects(OBJECTS_FILE)
    statuses = load_statuses(STATUSES_FILE)
    if not statuses:
        statuses = create_default_statuses()
    complaints = load_complaints(
        COMPLAINTS_FILE,
        users,
        objects,
        statuses,
    )

    while True:
        print("\n=== Система учета жалоб пользователей ===")
        print("1. Показать пользователей")
        print("2. Добавить пользователя")
        print("3. Найти пользователя")
        print("4. Показать объекты")
        print("5. Добавить объект")
        print("6. Найти объект")
        print("7. Показать статусы")
        print("8. Показать жалобы")
        print("9. Создать жалобу")
        print("10. Найти жалобу по описанию")
        print("11. Найти жалобы пользователя")
        print("12. Найти жалобы по статусу")
        print("13. Изменить статус жалобы")
        print("14. Сортировать жалобы")
        print("15. Статистика жалоб")
        print("0. Выход")

        choice = input_int("\nВыберите действие: ")

        if choice == 0:
            save_all(users, objects, statuses, complaints)
            print("Данные сохранены. Программа завершена.")
            break

        if choice == 1:
            show_users(users)
        elif choice == 2:
            name = input_non_empty("Введите имя пользователя: ")
            email = input_non_empty("Введите email: ")
            user = add_user(users, name, email)
            print(f"Пользователь добавлен: {user}")
        elif choice == 3:
            query = input_non_empty("Введите имя или email: ")
            result = find_user(users, query)
            if result:
                for user in result:
                    print(user)
            else:
                print("Пользователь не найден.")
        elif choice == 4:
            show_objects(objects)
        elif choice == 5:
            name = input_non_empty("Введите название объекта: ")
            description = input_non_empty("Введите описание объекта: ")
            item = add_object(objects, name, description)
            print(f"Объект добавлен: {item}")
        elif choice == 6:
            query = input_non_empty("Введите название объекта: ")
            result = find_object(objects, query)
            if result:
                for item in result:
                    print(f"{item} | {item.description}")
            else:
                print("Объект не найден.")
        elif choice == 7:
            for status in statuses:
                print(status)
        elif choice == 8:
            show_complaints(complaints)
        elif choice == 9:
            show_users(users)
            user_id = input_int("Введите ID пользователя: ")
            user = get_user_by_id(users, user_id)
            if user is None:
                print("Пользователь не найден.")
                continue
            show_objects(objects)
            object_id = input_int("Введите ID объекта: ")
            complaint_object = get_object_by_id(objects, object_id)
            if complaint_object is None:
                print("Объект не найден.")
                continue
            new_status = next(
                status for status in statuses if status.id == 1
            )
            description = input_non_empty("Введите описание проблемы: ")
            complaint = create_complaint(
                complaints,
                user,
                complaint_object,
                new_status,
                description,
            )
            print("\nЖалоба создана:")
            print(complaint)
        elif choice == 10:
            query = input_non_empty("Введите текст для поиска: ")
            show_results(find_complaint(complaints, query))
        elif choice == 11:
            user_id = input_int("Введите ID пользователя: ")
            show_results(find_complaints_by_user(complaints, user_id))
        elif choice == 12:
            status = choose_status(statuses)
            show_results(find_complaints_by_status(complaints, status.id))
        elif choice == 13:
            complaint_id = input_int("Введите ID жалобы: ")
            if get_complaint_by_id(complaints, complaint_id) is None:
                print("Жалоба не найдена.")
                continue
            status = choose_status(statuses)
            change_status(complaints, complaint_id, status)
            print("Статус жалобы изменен.")
        elif choice == 14:
            show_results(sort_complaints(complaints))
        elif choice == 15:
            statistics = complaint_statistics(complaints)
            print("\n--- Статистика ---")
            print(f"Всего жалоб: {len(complaints)}")
            for status, count in statistics.items():
                print(f"{status}: {count}")
        else:
            print("Ошибка: неизвестный пункт меню.")


if __name__ == "__main__":
    main()
