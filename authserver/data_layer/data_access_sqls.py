GET_USER_BY_EMAIL = """ 
SELECT email, password
FROM users
WHERE email=%s
"""
