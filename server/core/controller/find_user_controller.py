from core.services import FindUserService

class FindUserController:
    def handle(self, username):
        find_user_service = FindUserService()
        response = find_user_service.execute(username)
        
        if (response):
            return response
        else:
            return False
        