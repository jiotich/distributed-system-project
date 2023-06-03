import uuid

from passlib.hash  import sha256_crypt

from core.database import DatabaseInterface
from core.entities import User

class CreateUserService:
    def execute(self, username, password):
        
        id = uuid.uuid4()
        password_hash = sha256_crypt.hash(password)
        
        new_user = User()
        new_user.create_user(id, username, password_hash)
        
        interface = DatabaseInterface()
        
        user_already_exists = interface.user_exists(username)
        
        if (user_already_exists):
            return False
        else:
            interface.create_user(new_user)
            return True
