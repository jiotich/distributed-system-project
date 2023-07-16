from core.services import AuthUserService

class AuthUserController:
    def handle(self, username, password):
        authUserService = AuthUserService()
        response = authUserService.execute(username, password)
        
        if (response):
            return response
        else:
            return False