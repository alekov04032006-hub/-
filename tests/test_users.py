from users import add_user, find_user


def test_add_user():
    users = []
    user = add_user(users, "Александр", "alex@example.com")
    assert user["id"] == 1
    assert len(users) == 1


def test_find_user():
    users = []
    add_user(users, "Александр", "alex@example.com")
    assert find_user(users, "александр")[0]["id"] == 1
