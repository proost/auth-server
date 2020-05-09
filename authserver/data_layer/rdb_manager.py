import pymysql

from authserver.entity.user import User
from authserver.data_layer.data_access_sqls import GET_USER_BY_EMAIL 
from authserver.resources.config import RDB_HOST, RDB_PASSWORD, RDB_USER, RDB_NAME


class DbContextManagerBase:
    def __init__(self, optional_connector=None):
        if optional_connector:
            self.conn = optional_connector
        else:
            self.conn = pymysql.connect(
                host=RDB_HOST,
                user=RDB_USER,
                password=RDB_PASSWORD,
                db=RDB_NAME,
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor
            )

        self.cursor = self.conn.cursor()

    def get_user_by_email(self, user):
        try:
            self.cursor.execute(GET_USER_BY_EMAIL, (user.email))
            data = self.cursor.fetchone()
            return User(**data)
        except Exception as e:
            print(e)
            return None


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

    