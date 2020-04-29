import pytest
import pymysql

from authserver.entity.User import User, UserFromView
from authserver.resources.config import DB_HOST, DB_PASSWORD, DB_USER, DB_NAME
from authserver.data_layer.rdb_manager import (
    DbContextManager, DbContextManagerWithTxn
)


@pytest.fixture(scope="function")
def generate_connector():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    yield conn

def assert_user_equal(user1, user2):
    if user1.name != user2.name:
        return False
    
    if user1.password != user2.password:
        return False

    if user1.email != user2.email:
        return False

    return True

def test_create_user(generate_connector):
    user = UserFromView("tester3", "12345", "tester3@example.com")

    conn = generate_connector
    with DbContextManagerWithTxn(optional_connector=conn, is_test=True) as mgr:
        res = mgr.create_user(user) 
        assert res

def test_get_user_by_email(generate_connector):
    user = User(email="tester0@example.com")
    data = {
        "email": "tester0@example.com",
        "name": "tester0"
    }
    expect = User(**data)

    conn = generate_connector
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email(user)
        assert assert_user_equal(res, expect)

def test_get_user_by_email_not_found(generate_connector):
    user = User(email="tester000@example.com")

    conn = generate_connector
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email(user)
        assert res == None

def test_get_user_by_email_and_password(generate_connector):
    user = User(password="1234", email="tester0@example.com")
    data = {
        "email": "tester0@example.com",
        "name": "tester0"
    }
    expect = User(**data)

    conn = generate_connector
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email_and_password(user)
        assert assert_user_equal(res, expect)

def test_get_user_by_email_and_password_not_matched(generate_connector):
    user = User(password="12345", email="tester0@example.com")

    conn = generate_connector
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email_and_password(user)
        assert res == None

def test_change_user_by_email(generate_connector):
    conn = generate_connector
    user = UserFromView("tester0", "12345", "tester0example.com")

    with DbContextManagerWithTxn(optional_connector=conn, is_test=True) as mgr:
        res = mgr.change_user_by_email(user)
        assert res
