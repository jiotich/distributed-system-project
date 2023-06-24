import uuid

from passlib.hash         import sha256_crypt

# from misc.error_codes     import OK
# from misc.error_codes     import InvalidUsername
# from misc.error_codes     import UserExists

from misc.username_filter import UsernameFilter

from core.repositories    import UserRepository
from core.entities        import User

class CreateUserService:
    def execute(self, username, password, description):
        
        username_filter = UsernameFilter()
        
        if (username_filter.filter(username)):
        
            user_repository = UserRepository()
            
            id = uuid.uuid4()
            password_hash = sha256_crypt.hash(password)
            
            new_user = User(id, username, password_hash, description)
            user_already_exists = user_repository.find_one(username)
            
            if (user_already_exists):
                # return UserExists
                return 700
            else:
                user_repository.create(new_user)
                # return OK
                return True
        else:
            # return InvalidUsername
            return 701
