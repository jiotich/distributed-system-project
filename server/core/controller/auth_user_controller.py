import json

from core.services import AuthUserService

class AuthUserController:
    def handle(self, username, password):
        authUserService = AuthUserService()
        response = authUserService.execute(username, password)
        
        if (response):
            json.dumps({"status_code": 200, "token": response})
            
            #gerar o JSON com a resposta positiva
        else:
            #gerar o JSON com a resposta negativa
            json.dumps({"status_code": 400, "token": 0000})