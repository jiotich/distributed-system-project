from core.services import ListFollowedsService

class ListFollowedsController:
    def handle(self, follower_username): # retorna um array de posts
        list_followeds_service = ListFollowedsService()
        response = list_followeds_service.execute(follower_username)
        
        if (response):
            return response
        else:
            return False
        