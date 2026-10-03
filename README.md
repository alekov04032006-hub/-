# Система учета жалоб пользователей

## Назначение

Консольное приложение для регистрации и обработки жалоб пользователей на различные объекты.

## Основные сущности

- `User` — пользователь системы;
- `Complaint` — жалоба пользователя;
- `ComplaintObject` — объект, на который подается жалоба;
- `Status` — статус обработки жалобы.

## Основные классы

### User
Атрибуты: `id`, `name`, `email`.

Методы: `__init__()`, `from_data()`, `__str__()`.

### ComplaintObject
Атрибуты: `id`, `name`, `description`.

Методы: `__init__()`, `from_data()`, `__str__()`.

### Status
Атрибуты: `id`, `name`.

Методы: `__init__()`, `from_data()`, `__str__()`.

### Complaint
Атрибуты: `id`, `user`, `object`, `status`, `description`, `created_at`.

Методы: `__init__()`, `change_status()`, `__str__()`.

Объект `Complaint` связан с объектами `User`, `ComplaintObject` и `Status`.

## Основные возможности

- добавление и поиск пользователей;
- добавление и поиск объектов;
- создание жалоб;
- поиск жалоб;
- поиск жалоб пользователя;
- поиск жалоб по статусу;
- изменение статуса жалобы;
- сортировка жалоб;
- статистика по статусам;
- сохранение и загрузка данных в JSON.

## Структура проекта

```text
complaints_system/
├── README.md
├── main.py
├── users.py
├── objects.py
├── complaints.py
├── statuses.py
├── storage.py
├── utils.py
├── requirements.txt
├── pytest.ini
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── complaint_object.py
│   ├── status.py
│   └── complaint.py
├── data/
│   ├── users.json
│   ├── objects.json
│   ├── statuses.json
│   └── complaints.json
└── tests/
    ├── test_models.py
    └── test_functions.py
```

## Хранение данных

Данные хранятся в JSON-файлах. При загрузке данные преобразуются в объекты классов. При сохранении ссылки на связанные объекты заменяются их идентификаторами `user_id`, `object_id` и `status_id`.

## Запуск

```bash
python main.py
```

## Тестирование

```bash
pytest -v
```

## Проверка качества кода

```bash
flake8 .
```

## Git

Результат каждой практической работы сохраняется в общем Git-репозитории проекта.

## План развития

- разработка Django-приложения;
- подключение базы данных;
- реализация REST API;
- регистрация и авторизация пользователей;
- контейнеризация приложения.
