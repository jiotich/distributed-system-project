import sqlite3 as SQL

from core.entities import Post
from core.entities import User
from core.entities import Relationship
from core.entities import PostComentary

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
    
    def coment(self, comentary: PostComentary):
        try:
            connection = DatabaseConnection()

            cursor = connection.start_connection()
            cursor.execute(
                queries.CREATE_COMENTARY,
                [
                    comentary.id,
                    comentary.post_id,
                    comentary.user_id,
                    comentary.created_date,
                    comentary.created_time,
                    comentary.content
                ]
            )

            connection.commit_operation()
            connection.finish_connection()

        except SQL.IntegrityError:
            return False
        else:
            return True

    def like(self, id, user_id, post_id):
        try:
            connection = DatabaseConnection()

            cursor = connection.start_connection()
            cursor.execute(
                queries.LIKE_POST,
                [
                    id,
                    post_id,
                    user_id
                ]
            )

            connection.commit_operation()
            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else: 
            return True
        
    def unlike(self, user_id, post_id):
        try:
            connection = DatabaseConnection()

            cursor = connection.start_connection()
            cursor.execute(
                queries.UNLIKE_POST,
                [
                    user_id,
                    post_id
                ]
            )

            connection.commit_operation()
            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else: 
            return True

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
        
    def list_followers(self, followed_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.LIST_FOLLOWERS, 
                [
                    str(followed_id),
                ]
            )
            
            connection.commit_operation()
            retrived_data = cursor.fetchall()
            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data

    def list_followeds(self, follower_id):
        try:
            connection = DatabaseConnection()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.LIST_FOLLOWEDS, 
                [
                    str(follower_id),
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
                queries.DELETE_RELATIONSHIP, 
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