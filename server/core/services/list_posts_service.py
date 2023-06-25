from core.repositories import PostRepository
from core.repositories import UserRepository

from misc.sort         import Sort

#TODO: fazer os posts virem em ordem de data

class ListPostsService:
    def execute(self, username, target_username):
        user_repository = UserRepository()
        post_repository = PostRepository()
        
        user_exist        = user_repository.find_one(username)
        target_user_exist = user_repository.find_one(target_username)
        
        if (user_exist and target_username):
            caller_user_id = user_exist[0]
            target_user_id = target_user_exist[0]

            response = post_repository.find(
                caller_user_id,
                target_user_id
            )
            
            if (isinstance(response, list)):
                
                # sort = Sort()
                # ordered_responde = sort.order_by_date(response)

                return response
            else:
                return False
        else:
            return False