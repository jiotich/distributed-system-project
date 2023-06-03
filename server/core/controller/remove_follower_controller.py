from core.services import RemoveFollowerService

class RemoveFollowerController:
    def handle(self, followed_username, follower_username):
        remove_follower_service = RemoveFollowerService()
        response = remove_follower_service.execute(followed_username, follower_username)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass