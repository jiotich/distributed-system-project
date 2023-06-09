from core.repositories import UserRepository
from core.repositories import RelationshipRepository

class VerifyIfFollow:
    def execute(self, username, followed_username):
        
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()

        follower_user_exist = user_repository.find_one(username)
        followed_user_exist = user_repository.find_one(followed_username)

        
        if (follower_user_exist and followed_user_exist):
            follower_id  = follower_user_exist[0]
            followed_id  = followed_user_exist[0]

            response = relationship_repository.findfollowed(
                follower_id,
                followed_id
            )
            
            if (response):
                return True
            else:
                return False
        else:
            return False
        
        