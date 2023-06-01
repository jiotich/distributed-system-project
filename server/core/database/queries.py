ADD_USER           = """INSERT INTO user (id, username, password) VALUES (?,?,?)"""
VERIFY_USER_EXISTS    = """SELECT username, password FROM user WHERE username = (?)"""