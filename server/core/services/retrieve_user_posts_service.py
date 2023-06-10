from core.repositories import PostRepository
from core.repositories import UserRepository

from misc.sort         import Sort

#TODO: fazer os posts virem em ordem de data

class RetrieveUserPostsService:
    def execute(self, username):
        
        user_repository         = UserRepository()
        post_repository         = PostRepository()
        
        user_exist = user_repository.find_one(username)
        
        if (user_exist):
            user_id  = user_exist[0]

            response = post_repository.find(user_id)
            
            if (response):
                
                # sort = Sort()
                # ordered_responde = sort.order_by_date(response)

                return response
            else:
                return False
        else:
            return False