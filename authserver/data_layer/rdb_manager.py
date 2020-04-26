import pymysql

from authserver.data_layer.data_access_sqls import (
    GET_USER_BY_EMAIL, CREATE_USER, CHAGE_USER_BY_EMAIL
)
from authserver.resources.config import DB_HOST, DB_PASSWORD, DB_USER, DB_NAME


class DbManager:
    def __init__(self):
        self.conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset="utf8"
        )
    
    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, *args, **kwargs):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def get_user_by_email(email):
    with DbManager() as mgr:
        user = mgr.execute(GET_USER_BY_EMAIL, (email))
        return user

def create_user(name, password, email):
    with DbManager() as mgr:
        try:
            mgr.execute(CREATE_USER, (name, password, email))
            return True
        except Exception:
            return False

def change_user_by_email(name, password, email):
    with DbManager() as mgr:
        try:
            mgr.execute(CHAGE_USER_BY_EMAIL, (name, password, email))
            return True
        except Exception:
            return False
    