from core.services import RetrieveFeedService

class RetrieveFeedController:
    def handle(self, username, posts_limit=0): # retorna um array de posts
        retrieve_feed_service = RetrieveFeedService()
        response = retrieve_feed_service.execute(username, posts_limit)
        
        if (isinstance(response, list)):
            return response
        else:
            return False