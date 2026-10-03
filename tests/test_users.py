from users import add_user, find_user


def test_add_user():
    users = []

    user = add_user(
        users,
        "Александр",
        "alex@example.com",
    )

    assert user.id == 1
    assert user.name == "Александр"
    assert user.email == "alex@example.com"


def test_find_user():
    users = []

    add_user(
        users,
        "Александр",
        "alex@example.com",
    )

    result = find_user(
        users,
        "александр",
    )

    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].name == "Александр"
