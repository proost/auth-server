import pytest
import pymysql

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

def test_create_user(generate_connector):
    username = 'tester3'
    password = '12345'
    email = 'tester3@example.com'

    conn = generate_connector
    res = None
    with DbContextManagerWithTxn(optional_connector=conn, is_test=True) as mgr:
        res = mgr.create_user(username, password, email)
    
    assert res

def test_get_user_by_email(generate_connector):
    email = "tester0@example.com"
    expect = {
        "email": "tester0@example.com",
        "name": "tester0"
    }

    conn = generate_connector
    res = None
    with DbContextManager(optional_connector=conn) as mgr:
        res = mgr.get_user_by_email(email)
    
    assert res == expect

def test_change_user_by_email(generate_connector):
    conn = generate_connector
    email = "tester0@example.com"
    password = "12345"    
    name = "tester0"

    res = None
    with DbContextManagerWithTxn(optional_connector=conn, is_test=True) as mgr:
        res = mgr.change_user_by_email(name, password, email)
    
    assert res
