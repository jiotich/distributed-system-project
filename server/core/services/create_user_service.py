import uuid

from passlib.hash      import sha256_crypt

from core.repositories import UserRepository
from core.entities     import User

class CreateUserService:
    def execute(self, username, password):
        
        user_repository = UserRepository()
        
        id = uuid.uuid4()
        password_hash = sha256_crypt.hash(password)
        
        new_user = User(id, username, password_hash)
        
        user_already_exists = user_repository.find_one(username)
        
        if (user_already_exists):
            return False
        else:
            user_repository.create(new_user)
            return True
