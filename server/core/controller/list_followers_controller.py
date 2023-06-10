import json
from core.services import ListFollowersService

class ListFollowersController:
    def handle(self, followed_username): # retorna um array de posts
        list_followers_service = ListFollowersService()
        response = list_followers_service.execute(followed_username)
        
        if (response):
            return json.dumps({"data": response, "status_code": "200"})
        else:
            return json.dumps({"data": "", "status_code": "400"})