from core.repositories import PostRepository
from core.repositories import UserRepository
from core.repositories import RelationshipRepository

class RetrieveFeedService:
    def execute(self, username):
        
        user_repository         = UserRepository()
        post_repository         = PostRepository()
        relationship_repository = RelationshipRepository()
        
        user_exist = user_repository.find_one(username)
        
        if (user_exist):
            response = []
            user_id  = user_exist[0]

            followed_users = relationship_repository.find(user_id)
            
            for index in range(len(followed_users)):
                response.append(post_repository.find(followed_users[0][index]))
            
            return response[0]
        else:
            return False
        
        