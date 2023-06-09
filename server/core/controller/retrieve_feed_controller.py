import json
from core.services import RetrieveFeedService

class RetrieveFeedController:
    def handle(self, username, posts_limit=0): # retorna um array de posts
        retrieve_feed_service = RetrieveFeedService()
        response = retrieve_feed_service.execute(username, posts_limit)
        
        if (response):
            return json.dumps({"data": response, "status_code": "200"})
        else:
            return json.dumps({"data": "", "status_code": "400"})