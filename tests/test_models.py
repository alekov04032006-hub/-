from models import Complaint, ComplaintObject, Status, User


def make_models():
    user = User(1, "Александр", "alex@example.com")
    complaint_object = ComplaintObject(1, "Личный кабинет", "Раздел")
    status = Status(1, "Новая")
    return user, complaint_object, status


def test_user_creation_and_str():
    user, _, _ = make_models()
    assert user.id == 1
    assert str(user) == "1: Александр (alex@example.com)"


def test_user_from_data():
    user = User.from_data(
        {"id": 2, "name": "Анна", "email": "anna@example.com"}
    )
    assert user.id == 2
    assert user.name == "Анна"


def test_complaint_object_creation():
    _, complaint_object, _ = make_models()
    assert complaint_object.name == "Личный кабинет"
    assert str(complaint_object) == "1: Личный кабинет"


def test_complaint_creation_and_links():
    user, complaint_object, status = make_models()
    complaint = Complaint(
        1,
        user,
        complaint_object,
        status,
        "Проблема",
        "2026-10-02 16:00:00",
    )
    assert complaint.user is user
    assert complaint.object is complaint_object
    assert complaint.status is status


def test_complaint_change_status():
    user, complaint_object, status = make_models()
    complaint = Complaint(
        1,
        user,
        complaint_object,
        status,
        "Проблема",
        "2026-10-02 16:00:00",
    )
    new_status = Status(3, "Решена")
    complaint.change_status(new_status)
    assert complaint.status is new_status
