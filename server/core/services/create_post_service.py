import uuid
from datetime          import datetime

from core.repositories import PostRepository
from core.repositories import UserRepository
from core.entities     import Post
from core.entities     import Image

class CreatePostService:
    def execute(self, username, description, image):
        
        user_repository = UserRepository()
        post_repository = PostRepository()
        
        user_exist = user_repository.find_one(username)
        
        if (user_exist):
            user_id = user_exist[0]
            date = datetime.now().strftime("%d/%m/%Y")
            time = datetime.now().strftime("%H:%M:%S")
            
            post_id  = uuid.uuid4()
            image_id = uuid.uuid4()
            
            new_image = Image(image_id, image, date, time)
            new_post  = Post(post_id, user_id, description, 0, date, time, new_image)
            
            response = post_repository.create(new_post)
            
            return response
        else: 
            return False