import sqlite3 as SQL

from core.entities import Post
from core.database import DatabaseConnection
from core.database import queries

class PostRepository:
    def create(self, post: Post):
        image = post.get_image()
        
        connection = DatabaseConnection()
        
        cursor = connection.start_connection()
        cursor.execute(
            queries.CREATE_IMAGE, 
            [
                str(image.id), 
                str(image.data), 
                str(image.created_date), 
                str(image.created_time)
            ]
        )
        
        cursor.execute(
            queries.CREATE_POST,
            [
                str(post.id),
                str(post.owner_id),
                str(image.id),
                str(post.description),
                str(post.upvotes),
                str(post.created_date),
                str(post.created_time)
            ]
        )
        
        connection.commit_operation()
        connection.finish_connection()

class UserRepository:
    def find_one(self, username):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            cursor.execute(queries.VERIFY_USER_EXISTS, [str(username)])
            connection.commit_operation()
            
            retrived_data = cursor.fetchone()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data