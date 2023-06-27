from core.services import FindUserService

class FindUserController:
    def handle(self, username, target_user):
        find_user_service = FindUserService()
        response = find_user_service.execute(username, target_user)
        
        if (response):
            return response
        else:
            return False
        