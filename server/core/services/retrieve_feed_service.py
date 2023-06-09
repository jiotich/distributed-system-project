from core.repositories import PostRepository
from core.repositories import UserRepository
from core.repositories import RelationshipRepository

#TODO: fazer os posts virem em ordem de data

class RetrieveFeedService:
    def execute(self, username, posts_limit):
        
        user_repository         = UserRepository()
        post_repository         = PostRepository()
        relationship_repository = RelationshipRepository()
        
        user_exist = user_repository.find_one(username)
        
        if (user_exist):
            response = []
            posts = []
            user_id  = user_exist[0]

            followed_users = relationship_repository.find(user_id)
            
            for index in range(len(followed_users)):
                response.append(post_repository.find(followed_users[0][index]))
            
            if (response):
                if (posts_limit != 0):

                    if (len(response[0]) < posts_limit):
                        limit = len(response[0])
                    else:
                        limit = posts_limit

                    for index in range(limit):
                        posts.append(response[0][index])
                else:
                    posts = response[0]

                return posts
            else:
                return False
        else:
            return False
        
        