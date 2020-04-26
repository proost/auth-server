import pytest
from authserver.data_layer.rdb_manager import (
    get_user_by_email,
    create_user,
    change_user_by_email
)

def test_create_user():
    username = 'tester2'
    password = '1234'
    email = 'tester2@example.com'
    res = create_user(
        name=username, password=password, email=email
    )
    assert res

