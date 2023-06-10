import json

from core.services import AuthUserService

class AuthUserController:
    def handle(self, username, password):
        authUserService = AuthUserService()
        response = authUserService.execute(username, password)
        
        if (response):
            return json.dumps({
                "message": "success", 
                "status_code": "200", 
                "token": response
            })
        else:
            return json.dumps({
                "message": "failed", 
                "status_code": "400", 
                "token": "-1"
            })