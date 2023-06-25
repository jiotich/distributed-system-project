from core.services import VerifyLikedPostService

class VerifyLikedPostController:
    def handle(self, username, post_id): # retorna um array de posts
        verify_liked_post_service = VerifyLikedPostService()
        response = verify_liked_post_service.execute(username, post_id)
        
        return response