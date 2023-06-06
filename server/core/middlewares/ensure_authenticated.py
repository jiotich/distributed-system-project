import jwt

class EnsureAuthenticated:
    def __init__(self):
        self._jwt_secret    = "segredo"
        self._jwt_algorithm = "HS256"

    def handle(self, token, description, image):
        try:
            decoded = jwt.decode(
                jwt=token, 
                key=self._jwt_secret, 
                algorithms=self._jwt_algorithm
            )

            username = decoded[1]
        except jwt.PyJWTError:
            return False
        else:
            return username, description, image
