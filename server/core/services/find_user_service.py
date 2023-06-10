import uuid

#TODO: refazer 

from passlib.hash      import sha256_crypt
from core.repositories import UserRepository
 
class FindUserService:
    def execute(self, username):
        
        user_repository = UserRepository()
        
        user = user_repository.find_one(username)
        
        if (user):
            return user
        else:
            return False
