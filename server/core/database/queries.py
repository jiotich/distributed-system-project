ADD_USER              = """INSERT INTO user (id, username, password) VALUES (?,?,?)"""
VERIFY_USER_EXISTS    = """SELECT id, username, password FROM user WHERE username = (?)"""
CREATE_IMAGE          = """INSERT INTO image (id, data, created_date, created_time) VALUES (?,?,?,?)"""
CREATE_POST           = """INSERT INTO post (id, fk_post_user, fk_post_image, description, up_votes, created_date, created_time) VALUES (?,?,?,?,?,?,?)"""