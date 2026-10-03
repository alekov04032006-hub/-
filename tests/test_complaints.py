from complaints import (
    change_status,
    complaint_statistics,
    create_complaint,
)
from models import ComplaintObject, Status, User


def make_data():
    user = User(1, "Александр", "alex@example.com")
    complaint_object = ComplaintObject(
        1,
        "Личный кабинет",
        "Раздел сайта",
    )
    status = Status(1, "Новая")

    return user, complaint_object, status


def test_create_complaint():
    user, complaint_object, status = make_data()
    complaints = []

    complaint = create_complaint(
        complaints,
        user,
        complaint_object,
        status,
        "Не работает личный кабинет",
    )

    assert complaint.id == 1
    assert complaint.user is user
    assert complaint.object is complaint_object
    assert complaint.status is status
    assert len(complaints) == 1


def test_change_status():
    user, complaint_object, status = make_data()
    complaints = []

    create_complaint(
        complaints,
        user,
        complaint_object,
        status,
        "Проблема с входом",
    )

    new_status = Status(3, "Решена")

    result = change_status(
        complaints,
        1,
        new_status,
    )

    assert result is True
    assert complaints[0].status is new_status


def test_complaint_statistics():
    user, complaint_object, status = make_data()
    complaints = []

    create_complaint(
        complaints,
        user,
        complaint_object,
        status,
        "Проблема 1",
    )

    create_complaint(
        complaints,
        user,
        complaint_object,
        status,
        "Проблема 2",
    )

    statistics = complaint_statistics(complaints)

    assert statistics["Новая"] == 2
