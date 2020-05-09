from werkzeug.security import check_password_hash


def assert_user_equal(not_hashed_user, hashed_user):
    if not_hashed_user.name != hashed_user.name:
        return False
    
    if not check_password_hash(not_hashed_user.password, hashed_user.password):
        return False

    if not_hashed_user.email != hashed_user.email:
        return False

    return True