import uuid

from core.repositories import UserRepository
from core.repositories import RelationshipRepository
from core.entities     import Relationship

class CreateRelationshipService:
    def execute(self, follower_username, followed_username):
        
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()
        
        follow_relationship_id   = uuid.uuid4()
        followed_relationship_id = uuid.uuid4()
        
        # sao criadas duas relações, pois o  ato de seguir um usuario 
        # implica que o algo passar a ter um seguidor
        
        follow_relationship = Relationship(
            follow_relationship_id, 
            follower_username, 
            followed_username,
            "follow"
        )
        
        followed_relationship = Relationship(
            followed_relationship_id, 
            followed_username, 
            follower_username,
            "followed"
        )
        
        follower_user_exist = user_repository.find_one(follower_username)
        followed_user_exist = user_repository.find_one(followed_username)

        if (follower_user_exist and followed_user_exist):
            relationship_repository.create(follow_relationship)
            relationship_repository.create(followed_relationship)
            
            return True
        else:
            return False