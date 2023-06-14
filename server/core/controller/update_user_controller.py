from core.services import UpdateUserService

class UpdateUserController:
    def handle(self, username, data, column):
        update_user_service = UpdateUserService()
        response = update_user_service.execute(username, data, column)
        
        return response
        
        