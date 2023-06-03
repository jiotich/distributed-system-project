from core.services import CreateRelationshipService

class CreateUserController:
    def handle(self, follower_username, followed_username):
        create_relationship_service = CreateRelationshipService()
        response = create_relationship_service.execute(follower_username, followed_username)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass