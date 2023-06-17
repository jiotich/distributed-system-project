import jwt
import datetime

from passlib.hash import sha256_crypt

from core.repositories import UserRepository

class AuthUserService:
    def __init__(self):
        self._jwt_secret    = "segredo"
        self._jwt_algorithm = "HS256"

    def execute(self, username, password):  
        
        user_repository = UserRepository()
              
        user_exists = user_repository.find_one(username)

        if (user_exists):
            id            = user_exists[0]
            username      = user_exists[1]
            password_hash = user_exists[2]

            password_match = sha256_crypt.verify(secret=password, hash=password_hash)
            
            if (password_match):
                token = jwt.encode(
                    { 
                        "id": id, 
                        "username": username,
                        "hash": password_hash,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
                    }, 
                    key=self._jwt_secret, 
                    algorithm=self._jwt_algorithm
                )

                return token
            else:
                return False
        else:
            return False