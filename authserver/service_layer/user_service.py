from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
)
from werkzeug.security import check_password_hash

from authserver.entity.user import User
from authserver.data_layer.rdb_manager import DbContextManager, DbContextManagerWithTxn


class UserService:
    def __init__(self):
        self.rdb = RdbUserService
        self.no_sql = None

    def authenticate_user(self, user: User):
        return self.rdb.authenticate_user(user)

    def refresh_token(self, email):
        return create_access_token(identity=email, fresh=False)
    
class RdbUserService:
    @classmethod
    def authenticate_user(cls, user: User):
        with DbContextManager() as mgr:
            user_data = mgr.get_user_by_email(user)
            if check_password_hash(user_data.password, user.password):
                return {
                    "access_token": create_access_token(identity=user_data.email),
                    "refresh_token": create_refresh_token(identity=user_data.email),
                }
            else:
                return None
