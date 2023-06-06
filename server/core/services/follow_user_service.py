import uuid

from core.repositories import UserRepository
from core.repositories import RelationshipRepository
from core.entities     import Relationship

class FollowUserService:
    def execute(self, followed_username, follower_username):
        
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()
        
        follow_relationship_id   = uuid.uuid4()
        
        followed_user_exist = user_repository.find_one(followed_username)
        follower_user_exist = user_repository.find_one(follower_username)
        
        followed_user_id = followed_user_exist[0]
        follower_user_id = follower_user_exist[0]
        
        follow_relationship = Relationship(
            follow_relationship_id, 
            followed_user_id, 
            follower_user_id,
        )

        if (followed_user_exist and follower_user_exist):
            response = relationship_repository.create(follow_relationship)
            
            return response
        else:
            return False