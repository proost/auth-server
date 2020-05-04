import pytest
from werkzeug.security import check_password_hash

from authserver.entity.user import User, UserFromView

def test_user_from_view():
    result = UserFromView(
        name="tester0",
        password="1234",
        email="tester0@example.com"
    )
    assert check_password_hash(result.password, "1234")