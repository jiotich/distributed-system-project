from core.repositories import UserRepository

class UpdateUserService:
    def execute(self, username, data, column):
        
        user_repository = UserRepository()
        user_exist = user_repository.find_one(username)

        if (user_exist):
            user_id = user_exist[0]
    
            response = user_repository.update(
                user_id=user_id,
                column=column,
                new_value=data
            )
            
            return response # return True or False
        else:
            return False