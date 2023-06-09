import json
from core.services import RetrieveUserPostsService

class RetrieveUserPostsController:
    def handle(self, username): # retorna um array de posts
        retrieve_user_posts_service = RetrieveUserPostsService()
        response = retrieve_user_posts_service.execute(username)
        
        if (response):
            return json.dumps({"data": response, "status_code": "200"})
        else:
            return json.dumps({"data": "", "status_code": "400"})