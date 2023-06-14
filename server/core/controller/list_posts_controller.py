import json
from core.services import ListPostsService

class ListPostsController:
    def handle(self, username): # retorna um array de posts
        list_posts_service = ListPostsService()
        response = list_posts_service.execute(username)
        
        if (response):
            return response
        else:
            return False
        
        # if (response):
        #     return json.dumps({
        #         "message": "success", "data": response, "status_code": 200
        #     })
        # else:
        #     return json.dumps({
        #         "message": "failed", "data": "", "status_code": 400
        #     })