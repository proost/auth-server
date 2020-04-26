GET_USER_BY_EMAIL = """ 
SELECT name, email 
FROM users
WHERE email=%s
"""

CREATE_USER = """
INSERT INTO users (name, password, email)
values (%s, %s, %s)
"""

CHAGE_USER_BY_EMAIL = """
UPDATE users
SET name=%s, password=%s
WHERE email=%s
"""
