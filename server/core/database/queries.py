CREATE_USER           = """ INSERT INTO user (id, username, password) VALUES (?,?,?)"""
VERIFY_USER_EXISTS    = """ SELECT id, username, password FROM user WHERE username = (?)"""
CREATE_IMAGE          = """ INSERT INTO image (id, data, created_date, created_time) VALUES (?,?,?,?)"""
CREATE_POST           = """ INSERT INTO post (id, fk_post_user, fk_post_image, description, up_votes, created_date, created_time) VALUES (?,?,?,?,?,?,?)"""
CREATE_RELATIONSHIP   = """ INSERT INTO relationship (id, fk_relationship_user1, fk_relationship_user2, type) VALUES (?,?,?,?)"""
FETCH_RELATIONSHIPS   = """ SELECT fk_relationship_user2 FROM relationship WHERE fk_relationship_user1 = (?) AND type = (?)"""

FETCH_POSTS = """ 
    SELECT 
        post.id, 
        post.description, 
        post.up_votes, 
        post.created_date, 
        post.created_time,
        image.data,
        user.username
    FROM 
        post 
    INNER JOIN image ON image.id = post.fk_post_image
    INNER JOIN user  ON user.id = post.fk_post_user
    WHERE 
        fk_post_user = (?) 
    """