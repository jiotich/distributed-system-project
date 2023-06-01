import jwt

from passlib.hash import sha256_crypt

from core.database import DatabaseInterface

class AuthUserService:
    def __init__(self):
        self._jwt_secret    = "segredo"
        self._jwt_algorithm = "HS256"

    def execute(self, username, password):        
        interface = DatabaseInterface()
        user_exists = interface.user_exists(username, password)

        if (user_exists):
            username      = user_exists[0]
            password_hash = user_exists[1]

            password_match = sha256_crypt.verify(secret=password, hash=password_hash)
            
            if (password_match):
                token = jwt.encode({"username": username}, self._jwt_secret, algorithm=self._jwt_algorithm)

                return token
            else:
                return False
        else:
            return False