import pymysql

from authserver.data_layer.data_access_sqls import (
    GET_USER_BY_EMAIL, CREATE_USER, CHAGE_USER_BY_EMAIL
)
from authserver.resources.config import DB_HOST, DB_PASSWORD, DB_USER, DB_NAME


class DbContextManagerBase:
    def __init__(self, optional_connector=None):
        if optional_connector:
            self.conn = optional_connector
        else:
            self.conn = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                db=DB_NAME,
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor
            )

        self.cursor = self.conn.cursor()

    def get_user_by_email(self, email):
        try:
            self.cursor.execute(GET_USER_BY_EMAIL, (email))
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            return None

    def create_user(self, name, password, email):
        try:
            self.cursor.execute(CREATE_USER, (name, password, email))
            return True
        except Exception as e:
            print(e)
            return False

    def change_user_by_email(self, name, password, email):
        try:
            self.cursor.execute(CHAGE_USER_BY_EMAIL, (name, password, email))
            return True
        except Exception as e:
            print(e)
            return False


class DbContextManagerWithTxn(DbContextManagerBase):
    def __init__(self, optional_connector=None, is_test=False):
        super().__init__(optional_connector)
        self.is_test = is_test

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.is_test:
            self.conn.rollback()
        else:
            self.conn.commit()
        
        self.cursor.close()
        self.conn.close()


class DbContextManager(DbContextManagerBase):
    def __init__(self, optional_connector=None):
        super().__init__(optional_connector)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):      
        self.cursor.close()
        self.conn.close()

    