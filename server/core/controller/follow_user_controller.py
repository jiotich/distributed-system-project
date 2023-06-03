from core.services import FollowUserService

class FollowUserController:
    def handle(self, follower_username, followed_username):
        follow_user_service = FollowUserService
        response = follow_user_service.execute(follower_username, followed_username)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass