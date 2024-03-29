from core.services import CreateUserService

class CreateUserController:
    def handle(self, username, password, description):
        create_user_service = CreateUserService()
        response = create_user_service.execute(username, password, description)
        
        return response
    