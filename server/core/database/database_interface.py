import sqlite3 as SQL

from core.database import DatabaseConnection
from core.database import queries
from core.entities import User

class DatabaseInterface:
    def __init__(self):
        pass
    
    def create_user(self, user: User):
        try: 
            id, username, password = user.get_user_info()
            connection = DatabaseConnection("./core/database/database.db")
            
            cursor = connection.start_connection()
            cursor.execute(queries.ADD_USER, [str(id), str(username), str(password)])
            
            connection.commit_operation()
            connection.finish_connection()
        
        except SQL.IntegrityError:
            return 400 # Bad Request
        else:
            return 201 # Created
    
    def user_exists(self, username, password):
        try: 
            connection = DatabaseConnection("./core/database/database.db")

            cursor = connection.start_connection()
            cursor.execute(queries.VERIFY_USER_EXISTS, [str(username)])
            connection.commit_operation()
            
            retrived_data = cursor.fetchone()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data
