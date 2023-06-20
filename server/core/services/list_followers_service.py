from core.repositories import RelationshipRepository
from core.repositories import UserRepository

class ListFollowersService:
    def execute(self, followed_username):
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()

        user_exist = user_repository.find_one(followed_username)
        
        if (user_exist):
            user_id  = user_exist[0]

            response = relationship_repository.list_followers(user_id)

            # verifica se é uma lista, pois mesmo se vazia a requisição devera retornar sucesso
            if (isinstance(response, list)):
                return response
            else:
                return False
        else:
            return False
