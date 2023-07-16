from core.repositories import RelationshipRepository
from core.repositories import UserRepository

class ListFollowedsService:
    def execute(self, follower_username):
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()

        user_exist = user_repository.find_one(follower_username)
        
        if (user_exist):
            user_id  = user_exist[0]

            response = relationship_repository.list_followeds(user_id)

            if (isinstance(response, list)):
                return response
            else:
                return False
        else:
            return False