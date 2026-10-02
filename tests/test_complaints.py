from complaints import (
    change_status,
    complaint_statistics,
    create_complaint,
)


def test_create_complaint():
    complaints = []
    complaint = create_complaint(
        complaints,
        1,
        1,
        "Не работает личный кабинет",
    )
    assert complaint is not None
    assert complaint["status"] == "Новая"
    assert len(complaints) == 1


def test_change_status():
    complaints = []
    create_complaint(complaints, 1, 1, "Проблема с входом")
    assert change_status(complaints, 1, "Решена")
    assert complaints[0]["status"] == "Решена"


def test_complaint_statistics():
    complaints = []
    create_complaint(complaints, 1, 1, "Проблема 1")
    create_complaint(complaints, 2, 1, "Проблема 2")
    change_status(complaints, 2, "Решена")
    statistics = complaint_statistics(complaints)
    assert statistics["Новая"] == 1
    assert statistics["Решена"] == 1
