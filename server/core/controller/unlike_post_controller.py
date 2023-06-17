from core.services import UnlikePostsService

class UnlikePostController:
    def handle(self, username, post_id):
        unlike_post_service = UnlikePostsService()
        response = unlike_post_service.execute(username, post_id)
        
        return response