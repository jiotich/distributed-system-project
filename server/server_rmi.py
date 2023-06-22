import sys
sys.dont_write_bytecode = True
import socket
import time

from Pyro5 import api as API

from nameserver import NameServer
from thread_pool import ThreadPool

from core.controller  import CreateUserController
from core.controller  import CreatePostController
from core.controller  import FollowUserController
from core.controller  import AuthUserController
from core.controller  import RetrieveFeedController
from core.controller  import RemoveFollowerController
from core.controller  import RemoveFollowedController
from core.controller  import ListPostsController
from core.controller  import ListFollowersController
from core.controller  import ListFollowedsController
from core.controller  import FindUserController
from core.controller  import UpdateUserController

from core.middlewares import EnsureAuthenticated

@API.expose
class UserRemoteObject:
    def __init__(self):
        self._create_user_controller     = CreateUserController()
        self._auth_user_controller       = AuthUserController()
        self._find_user_controller       = FindUserController()
        self._update_user_controller     = UpdateUserController()
        self._follow_user_controller     = FollowUserController()
        self._list_followers_controller  = ListFollowersController()
        self._list_followeds_controller  = ListFollowedsController()
        self._remove_follower_controller = RemoveFollowerController()
        self._remove_followed_controller = RemoveFollowedController()

        self._ensure_authenticated       = EnsureAuthenticated()
    
    def create_user(self, username, passord, description):

        response = self._create_user_controller.handle(
            username,
            passord,
            description
        )
        return response
        
    def auth_user(self, username, password):
        response = self._auth_user_controller.handle(
            username,
            password
        )
        return response
    
    def find_user(self, username, token):

        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            response = self._find_user_controller.handle(
                username
            )
            return response
        else:
            return False
        
    def update_user_description(self, username, new_description, token):
            
        authed = self._ensure_authenticated(token, username)
            
        if (authed):
            response = self._update_user_controller.handle(
                username,
                new_description,
                column="description"
            )
            return response
        else:
            return False
    
    def follow_user(self, followed_username, follower_username, token):

        authed = self._ensure_authenticated(token, followed_username)

        if (authed):
            response = self._follow_user_controller.handle(
                followed_username,
                follower_username
            )
            return response
        else:
            return False

    def list_user_followers(self, followed_username, token):

        authed = self._ensure_authenticated.handle(token, followed_username)

        if (authed):
            response = self._list_followers_controller.handle(
                followed_username
            )
            return response
        else:
            return False 
    
    def list_user_followeds(self, follower_username, token):

        authed = self._ensure_authenticated.handle(
            token,
            follower_username
        )

        if (authed):
            response = self._list_followeds_controller.handle(
                follower_username
            )
            return response
        else:
            return False

    def remove_user_follower(self, followed_username, follower_username, token):
        
        authed = self._ensure_authenticated.handle(token, followed_username)

        if (authed):
            response = self._remove_follower_controller.handle(
                followed_username,
                follower_username
            )
            return response
        else:
            return False
    
    def remove_user_followed(self, followed_username, follower_username, token):

        authed = self._ensure_authenticated.handle(token, follower_username)

        if (authed):
            response = self._remove_followed_controller.handle(
                follower_username,
                followed_username
            )
            return response 
        return False
       
        
@API.expose      
class PostRemoteObject:
    def __init__(self):
        self._create_post_controller   = CreatePostController()
        self._list_posts_controller    = ListPostsController()
        self._retrieve_feed_controller = RetrieveFeedController()

        self._ensure_authenticated     = EnsureAuthenticated()

    def create_post(self, username, description, image, token):

        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            response = self._create_post_controller.handle(
                username,
                description,
                image
            )
            return response
        else:
            return False

    def list_posts(self, username, token):

        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            response = self._list_posts_controller.handle(
                username
            )
            return response
        else:
            return False
    
    def retrieve_feed(self, username, post_limit, token):

        authed = self._ensure_authenticated.handle()

        if (authed):
            response = self._retrieve_feed_controller.handle(
                username,
                post_limit
            )
            return response
        else:
            return False




if (__name__ == "__main__"):

    thread_pool = ThreadPool()

    HOSTNAME = socket.gethostname()

    
    user_remote_object_nameserver = NameServer()
    # post_remote_object_nameserver = NameServer()


    d = user_remote_object_nameserver.start(
        remote_object=UserRemoteObject(),
        name="user_remote_object",
        port=49150,
    )

    def loopcondition():
        print(time.asctime(), "Waiting for requests...")
        return True


    d.requestLoop()

    # post_remote_object_nameserver.start(
    #     remote_object=PostRemoteObject(),
    #     name="post_remote_object",
    #     port=49155,
    # )


# Inicie o daemon do Pyro5
# Pyro5.api.daemon = Pyro5.api.Daemon()

# user_remote_obj = UserRemoteObject()
# post_remote_obj = PostRemoteObject()

# user_remote_obj_interface_uri = Pyro5.api.daemon.register(user_remote_obj)
# post_remote_obj_interface_uri = Pyro5.api.daemon.register(post_remote_obj)

# Pyro5.api.start_ns()

# print(user_remote_obj_interface_uri)
# # Inicie o loop do servidor para aguardar chamadas
# Pyro5.api.daemon.requestLoop()