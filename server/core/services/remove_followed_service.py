from core.repositories import UserRepository
from core.repositories import RelationshipRepository

class RemoveFollowedService:
    def execute(self, follower_username, followed_username):
        
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()
        
        follower_user_exist = user_repository.find_one(follower_username)
        followed_user_exist = user_repository.find_one(followed_username)
        
        followed_user_id = follower_user_exist[0]
        follower_user_id = followed_user_exist[0]
        
        if (followed_user_exist and follower_user_exist):
            response = relationship_repository.delete(
                follower_user_id, 
                followed_user_id
            )
            
            return response
        else:
            return False