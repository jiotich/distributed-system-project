import uuid
from core.repositories import UserRepository
 
class FindUserService:
    def execute(self, username):
        
        user_repository = UserRepository()
        user = user_repository.find_one(username)
        
        if (user):
            #removendo o hash da senha para retornar o usuário
            user_id          = user[0]
            user_name        = user[1]
            user_description = user[3]
        
            filtered_user = (user_id, user_name, user_description)
            
            return filtered_user
        else:
            return False
