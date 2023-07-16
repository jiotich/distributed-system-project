import uuid
from datetime          import datetime

from core.repositories import PostRepository
from core.repositories import UserRepository
from core.entities     import PostComentary

class ComentPostService:
    def execute(self, username, post_id, content):
        
        user_repository = UserRepository()
        post_repository = PostRepository()
        
        user_exist = user_repository.find_one(username)
        
        if (user_exist):
            user_id = user_exist[0]
            date = datetime.now().strftime("%d/%m/%Y")
            time = datetime.now().strftime("%H:%M:%S")
            
            comentary_id  = uuid.uuid4()
            
            new_comentary = PostComentary(
                comentary_id,
                user_id,
                post_id,
                date,
                time, 
                content
            )
            
            response = post_repository.coment(new_comentary)
            
            return response
        else: 
            return False
    