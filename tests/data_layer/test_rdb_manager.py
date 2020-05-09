import pytest
import pymysql

from authserver.entity.user import User, UserToRegister
from authserver.resources.config import RDB_HOST, RDB_PASSWORD, RDB_USER, RDB_NAME
from tests.utilites import assert_user_equal
from authserver.data_layer.rdb_manager import (
    DbContextManager, DbContextManagerWithTxn
)


@pytest.fixture(scope="function")
def generate_connector():
    conn = pymysql.connect(
        host=RDB_HOST,
        user=RDB_USER,
        password=RDB_PASSWORD,
        db=RDB_NAME,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    yield conn


def test_get_user_by_email(generate_connector):
    user = User(password="1234", email="tester0@example.com")
    data = {
        "email": "tester0@example.com",
        "password": "1234"
    }
    expect = User(**data)

    conn = generate_connector
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email(user)
        assert assert_user_equal(res, expect)

def test_get_user_by_email_not_matched(generate_connector):
    user = User(email="tester00@example.com")

    conn = generate_connector
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email(user)
        assert res == None
