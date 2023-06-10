import json

from core.services import AuthUserService

class AuthUserController:
    def handle(self, username, password):
        authUserService = AuthUserService()
        response = authUserService.execute(username, password)
        
        if (response):
            return json.dumps({
                "message": "success", 
                "token": response,
                "status_code": 200
            })
        else:
            return json.dumps({
                "message": "failed", 
                "token": "-1",
                "status_code": 400
            })