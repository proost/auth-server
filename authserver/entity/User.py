from werkzeug.security import generate_password_hash


class User:
    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email

    def encrypt_password(self, password):
        if password:
            return generate_password_hash(password)
        else:
            return None


class UserFromView(User):
    def __init__(self, name=None, password=None, email=None):
        encrypted_pw = super().encrypt_password(password)
        super().__init__(name=name, password=encrypted_pw, email=email)

