from complaints import (
    complaint_statistics,
    create_complaint,
    find_complaints_by_user,
)
from models import ComplaintObject, Status, User
from users import add_user, find_user


def test_add_and_find_user():
    users = []
    add_user(users, "Александр", "alex@example.com")
    assert find_user(users, "александр")[0].id == 1


def test_create_complaint():
    users = [User(1, "Александр", "alex@example.com")]
    objects = [ComplaintObject(1, "Личный кабинет", "Раздел")]
    new_status = Status(1, "Новая")
    complaints = []
    complaint = create_complaint(
        complaints,
        users[0],
        objects[0],
        new_status,
        "Не работает",
    )
    assert complaint.user is users[0]
    assert len(complaints) == 1


def test_find_complaints_by_user():
    users = [User(1, "Александр", "alex@example.com")]
    objects = [ComplaintObject(1, "Личный кабинет", "Раздел")]
    new_status = Status(1, "Новая")
    complaints = []
    create_complaint(
        complaints,
        users[0],
        objects[0],
        new_status,
        "Не работает",
    )
    assert len(find_complaints_by_user(complaints, 1)) == 1


def test_statistics():
    users = [User(1, "Александр", "alex@example.com")]
    objects = [ComplaintObject(1, "Личный кабинет", "Раздел")]
    new_status = Status(1, "Новая")
    complaints = []
    create_complaint(
        complaints,
        users[0],
        objects[0],
        new_status,
        "Проблема 1",
    )
    create_complaint(
        complaints,
        users[0],
        objects[0],
        new_status,
        "Проблема 2",
    )
    assert complaint_statistics(complaints)["Новая"] == 2
