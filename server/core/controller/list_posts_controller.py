from core.services import ListPostsService

class ListPostsController:
    def handle(self, username, target_username): # retorna um array de posts
        list_posts_service = ListPostsService()
        response = list_posts_service.execute(username, target_username)
        
        if (isinstance(response, list)):
            return response
        else:
            return False