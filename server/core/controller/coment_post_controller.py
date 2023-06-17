from core.services import ComentPostService

class ComentUserController:
    def handle(self, username, post_id, content):
        coment_post_service = ComentPostService()
        response = coment_post_service.execute(username, post_id, content)
        
        return response