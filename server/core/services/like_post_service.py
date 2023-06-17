import uuid

from core.repositories import PostRepository
from core.repositories import UserRepository

class LikePostsService:
    def execute(self, username, post_id):
        
        user_repository = UserRepository()
        post_repository = PostRepository()

        like_id = uuid.uuid4()  
        user_exist = user_repository.find_one(username)

        if (user_exist):
            user_id = user_exist[0]
            response = post_repository.like(
                like_id,
                user_id,
                post_id
            )
            return response
        else:
            return False