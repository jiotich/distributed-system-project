import uuid
from passlib.hash import sha256_crypt

from database import DatabaseInterface
from entities import User

class CreateUserService:
    def __init__(self):
        pass
    def execute(self, username, password):
        
        id = uuid.uuid4()
        password_hash = sha256_crypt.hash(password)
        
        new_user = User()
        new_user.create_user(id, username, password_hash)
        
        interface = DatabaseInterface()
        code = interface.create_user(new_user)
        
        return code