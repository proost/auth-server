def assert_user_equal(user1, user2):
    if user1.name != user2.name:
        return False
    
    if user1.password != user2.password:
        return False

    if user1.email != user2.email:
        return False

    return True