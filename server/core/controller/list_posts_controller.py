import json
from core.services import ListPostsService

class ListPostsController:
    def handle(self, username): # retorna um array de posts
        list_posts_service = ListPostsService()
        response = list_posts_service.execute(username)
        
        if (response):
            return json.dumps({"data": response, "status_code": "200"})
        else:
            return json.dumps({"data": "", "status_code": "400"})