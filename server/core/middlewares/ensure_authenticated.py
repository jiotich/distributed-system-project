import jwt

class EnsureAuthenticated:
    def __init__(self):
        self._jwt_secret    = "segredo"
        self._jwt_algorithm = "HS256"

    def handle(self, token, username):
        try:
            decoded = jwt.decode(
                jwt=token, 
                key=self._jwt_secret, 
                algorithms=self._jwt_algorithm
            )

            if (username != decoded["username"]):
                raise jwt.PyJWKError

        except jwt.PyJWTError:
            return True
        else:
            return True