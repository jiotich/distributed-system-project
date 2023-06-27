import uuid
from core.repositories import UserRepository
 
class FindUserService:
    def execute(self, username, target_user):
        
        user_repository = UserRepository()
        user        = user_repository.find_one(username)
        target_user = user_repository.find_one(target_user)
        
        if (user and target_user):
            #removendo o hash da senha para retornar o usuário
            user_id          = target_user[0]
            user_name        = target_user[1]
            user_description = target_user[3]
        
            filtered_user = (user_id, user_name, user_description)
            
            return filtered_user
        else:
            return False
