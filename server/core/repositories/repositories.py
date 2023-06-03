import sqlite3 as SQL

from core.entities import Post
from core.entities import User
from core.entities import Relationship

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

    def find(self, user_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            cursor.execute(
                queries.FETCH_POSTS, 
                [
                    str(user_id)
                ]
            )
            connection.commit_operation()
            
            retrived_data = cursor.fetchall()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            if (len(retrived_data) == 0):
                return False
            else:
                return retrived_data
        
        
class UserRepository:
    def find_one(self, username):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            cursor.execute(
                queries.VERIFY_USER_EXISTS, 
                [
                    str(username)
                ]
            )
            connection.commit_operation()
            
            retrived_data = cursor.fetchone()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data
    
    def create(self, user: User):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            cursor.execute(queries.CREATE_USER, [str(user.id), str(user.username), str(user.password)])
            connection.commit_operation()
            
            retrived_data = cursor.fetchone()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data
        
class RelationshipRepository:
    def create(self, relationship: Relationship):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.CREATE_RELATIONSHIP, 
                [
                    str(relationship.id), 
                    str(relationship.source_user),    
                    str(relationship.destination_user),
                    str(relationship.type)
                ]
            )
            
            connection.commit_operation()
            
            retrived_data = cursor.fetchone()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data
        
    def find(self, user_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            # retorna os ids dos usuarios que o usuário que foi fornecido o id segue
            
            cursor.execute(
                queries.FETCH_RELATIONSHIPS, 
                [
                    str(user_id),
                    str("follow")
                ]
            )
            
            connection.commit_operation()
            
            retrived_data = cursor.fetchall()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data