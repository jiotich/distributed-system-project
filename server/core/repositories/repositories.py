import sqlite3 as SQL

from core.entities import Post
from core.entities import User
from core.entities import Relationship

from core.database import DatabaseConnection
from core.database import queries

class PostRepository:
    def create(self, post: Post):
        try:
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
            
        except SQL.IntegrityError:
            return False
        else: 
            return True

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
            cursor.execute(
                queries.CREATE_USER, 
                [
                    str(user.id), 
                    str(user.username), 
                    str(user.password),
                    str(user.description)
                ]
            )

            connection.commit_operation()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return True
    
    def update(self, user_id, column, new_value):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            cursor.execute(
                queries.UPDATE_USER_COLUMNS, 
                [
                    str(column), 
                    str(new_value), 
                    str(user_id),
                ]
            )

            connection.commit_operation()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return True

class RelationshipRepository:
    def create(self, relationship: Relationship):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.CREATE_RELATIONSHIP, 
                [
                    str(relationship.id), 
                    str(relationship.followed),    
                    str(relationship.follower)
                ]
            )
            
            connection.commit_operation()
            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return True
        
    def find(self, user_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.FETCH_RELATIONSHIPS, 
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
            return retrived_data
        
    def findfollowed(self, follower_id, followed_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.VERIFY_IF_FOLLOW, 
                [
                    str(follower_id),
                    str(followed_id)
                    
                ]
            )
            
            connection.commit_operation()
            
            retrived_data = cursor.fetchall()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data
    
    def delete(self, followed_id, follower_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.REMOVE_FOLLOWER, 
                [
                    str(followed_id),
                    str(follower_id)
                ]
            )
            
            connection.commit_operation()
            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return True