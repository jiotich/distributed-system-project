import json
from core.services import ListFollowedsService

class ListFollowedsController:
    def handle(self, follower_username): # retorna um array de posts
        list_followeds_service = ListFollowedsService()
        response = list_followeds_service.execute(follower_username)
        
        if (response):
            return json.dumps({
                "message": "success", "data": response, "status_code": 200
            })
        else:
            return json.dumps({
                "message": "failed", "data": "", "status_code": 400
            })