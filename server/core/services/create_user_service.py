import uuid
import time
from passlib.hash         import sha256_crypt
from misc.username_filter import UsernameFilter
from core.repositories    import UserRepository
from core.entities        import User

class CreateUserService:
    def execute(self, username, password, description):
        
        username_filter = UsernameFilter()
        
        if (username_filter.filter(username)):
        
            user_repository = UserRepository()
            user_already_exists = user_repository.find_one(username)
            
            if (user_already_exists):
                # return UserExists
                return 700
            else:
                inicio = time.time()
                id = uuid.uuid4()
                fim1 = time.time()
                password_hash = sha256_crypt.hash(password)
                fim2 = time.time()
                new_user = User(id, username, password_hash, description)
                user_repository.create(new_user)
                fim3 = time.time()
                
                # print(f"tempo gerar uuid   : {fim1 - inicio}")
                # print(f"tempo gerar hash   : {fim2 - inicio}")
                # print(f"tempo criar usuario: {fim3 - inicio}")
                
                # return OK
                return 200
        else:
            # return InvalidUsername
            return 701
