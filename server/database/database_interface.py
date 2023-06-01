import sqlite3 as SQL

from database import DatabaseConnection
from database import queries
from entities import User

class DatabaseInterface:
    def __init__(self):
        pass
    def create_user(self, user: User):
        try: 
            id, username, password = user.get_user_info()
            connection = DatabaseConnection("./database/database.db")
            
            cursor = connection.start_connection()
            cursor.execute(queries.ADD_USER, [str(id), str(username), str(password)])
            
            connection.commit_operation()
            connection.finish_connection()
        
        except SQL.IntegrityError:
            return 400 # Bad Request
        else:
            return 201 # Created
        