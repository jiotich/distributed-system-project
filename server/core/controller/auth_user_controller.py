from core.services import AuthUserService

class AuthUserController:
    def handle(self, username, password):
        authUserService = AuthUserService()
        response = authUserService.execute(username, password)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass