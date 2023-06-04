import json

from core.services import AuthUserService

class AuthUserController:
    def handle(self, username, password):
        authUserService = AuthUserService()
        response = authUserService.execute(username, password)
        
        if (response):
            return json.dumps({"status_code": "200", "token": f"{response}"})
            
            #gerar o JSON com a resposta positiva
        else:
            #gerar o JSON com a resposta negativa
            return json.dumps({"status_code": "400", "token": "-1"})