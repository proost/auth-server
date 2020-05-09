from dataclasses import dataclass, field
from werkzeug.security import generate_password_hash


@dataclass
class User:
    name: str = field(default=None)
    password: str = field(default=None)
    email: str = field(default=None)

    @classmethod
    def encrypt_password(cls, password):
        if password:
            return generate_password_hash(password)
        else:
            return None


@dataclass
class UserToRegister(User):
    def __post_init__(self):
        self.password = super().encrypt_password(self.password)

