from core.services import LikePostsService

class LikePostController:
    def handle(self, username, post_id):
        like_post_service = LikePostsService()
        response = like_post_service.execute(username, post_id)
        
        return response