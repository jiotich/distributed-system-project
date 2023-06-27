CREATE_USER = """ 
    INSERT INTO user (
        id, 
        username, 
        password, 
        description
    ) VALUES (?,?,?,?)
"""

UPDATE_USER_COLUMNS = """
    UPDATE user
    SET 
        description = (?)
    WHERE
        id = (?)
"""

VERIFY_USER_EXISTS = """ 
    SELECT 
        id, username, password, description 
    FROM 
        user 
    WHERE username = (?)
"""

CREATE_IMAGE = """ 
    INSERT INTO image (
        id, 
        data, 
        created_date, 
        created_time
    ) VALUES (?,?,?,?)
"""

CREATE_POST = """ 
    INSERT INTO post (
        id, 
        fk_post_user, 
        fk_post_image, 
        description, 
        up_votes, 
        created_date, 
        created_time
    ) VALUES 
        (?,?,?,?,?,?,?)
"""

# TODO: Retornar os comentarios na query
    
FETCH_POSTS = """
    SELECT 
        post.id, 
        post.description, 
        post.up_votes, 
        post.created_date, 
        post.created_time,
        image.data,
        user.username,
        user.description,
        (SELECT COUNT(*) FROM post_like WHERE fk_like_user = (?) AND fk_like_post = post.id) AS is_liked
    FROM 
        post 
    INNER JOIN image ON image.id = post.fk_post_image
    INNER JOIN user ON user.id = post.fk_post_user
    WHERE 
        post.fk_post_user = (?);
"""
    
    
    
CREATE_RELATIONSHIP = """ 
    INSERT INTO 
        follow_relationship (id, fk_relationship_user_followed, fk_relationship_user_follower) 
    VALUES (?,?,?)
"""
    
DELETE_RELATIONSHIP = """
    DELETE FROM 
        follow_relationship
    WHERE
        fk_relationship_user_followed = (?) 
    AND
        fk_relationship_user_follower = (?) 
"""

LIST_FOLLOWERS = """
    SELECT 
        fk_relationship_user_follower
    FROM 
        follow_relationship 
    WHERE fk_relationship_user_followed = (?)
"""

LIST_FOLLOWEDS = """
    SELECT 
        fk_relationship_user_followed
    FROM 
        follow_relationship 
    WHERE fk_relationship_user_follower = (?)
"""

VERIFY_ALREADY_FOLLOW = """
    SELECT 
        id
    FROM 
        follow_relationship
    WHERE 
        fk_relationship_user_followed = (?)
    AND 
        fk_relationship_user_follower = (?)
"""

CREATE_COMENTARY = """
    INSERT INTO post_comentary (
        id,
        fk_comentary_post,
        fk_comentary_user,
        created_date,
        created_time,
        content
    ) VALUES (?,?,?,?)
"""

LIKE_POST = """
    INSERT INTO post_like (
        id, 
        fk_like_post, 
        fk_like_user
    )
    SELECT (?), (?), (?)
    WHERE NOT EXISTS (
        SELECT 1 FROM post_like
        WHERE 
            fk_like_post = (?) 
        AND 
            fk_like_user = (?)
)
"""

VERIFY_IF_LIKED = """
    SELECT EXISTS (
        SELECT 1 
        FROM 
            post_like 
        WHERE 
            fk_like_user = (?)
        AND
            fk_like_post = (?)
    ) AS exists_record; 
"""

UNLIKE_POST = """
    DELETE FROM
        post_like
    WHERE 
        fk_like_user = (?)
    AND
        fk_like_post = (?)
"""

INCREMENT_UPVOTE = """
    UPDATE 
        post
    SET 
        up_votes = up_votes + 1
    WHERE 
        id = (?);
"""

DECREMENT_UPVOTE = """
    UPDATE 
        post
    SET 
        up_votes = up_votes - 1
    WHERE 
        id = (?);
"""