from core.repositories import UserRepository
from core.repositories import RelationshipRepository

class RemoveFollowerService:
    def execute(self, followed_username, follower_username):
        
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()
        
        followed_user_exist = user_repository.find_one(followed_username)
        follower_user_exist = user_repository.find_one(follower_username)
        
        follower_user_id = follower_user_exist[0]
        followed_user_id = followed_user_exist[0]
        
        if (followed_user_exist and follower_user_exist):
            response = relationship_repository.delete(
                followed_user_id, 
                follower_user_id
            )
            
            return response
        else:
            return False