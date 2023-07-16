from core.services import ListFollowersService

class ListFollowersController:
    def handle(self, followed_username): # retorna um array de posts
        list_followers_service = ListFollowersService()
        response = list_followers_service.execute(followed_username)
        
        if (isinstance(response, list)):
            return response
        else:
            return False
