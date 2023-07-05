import sys
sys.dont_write_bytecode = True
import socket
import time

from Pyro5            import api as API
from nameserver       import NameServer
from thread_pool      import ThreadPool
from log              import Logger
from misc.load_config import Configs


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
from core.controller  import ComentPostController
from core.controller  import LikePostController
from core.controller  import UnlikePostController

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
        self._logger                     = Logger()
        
        self._object_name = "User Remote Object"
    
    def create_user(self, username, passord, description):
        begin = time.time()
        response = self._create_user_controller.handle(
            username,
            passord,
            description
        )
        
        self._logger.new_rmi_log(
            user_ip_address = "ip default de testes",
            username        = username,
            bytes_sent      = 0,
            bytes_received  = 0,
            time_spent      = time.time() - begin,
            nameserver      = "nameserver",
            object_name     = self._object_name,
            object_method   = "create_user",
            response_status = "response"
        )
        
        return response
        
    def auth_user(self, username, password):
        begin = time.time()
        response = self._auth_user_controller.handle(
            username,
            password
        )

        self._logger.new_rmi_log(
            user_ip_address = "ip default de testes",
            username        = username,
            bytes_sent      = 0,
            bytes_received  = 0,
            time_spent      = time.time() - begin,
            nameserver      = "nameserver",
            object_name     = self._object_name,
            object_method   = "auth_user",
            response_status = response
        )
        
        return response
    
    def find_user(self, username, target_user, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            response = self._find_user_controller.handle(
                target_user
            )
            
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "find_user",
                response_status = "response"
            )
            
            return response
        else:
            return False
        
    def update_user_description(self, username, new_description, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)
            
        if (authed):
            response = self._update_user_controller.handle(
                username,
                new_description,
            )
            
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "update_user_description",
                response_status = "response"
            )
            
            return response
        else:
            return False
    
    def follow_user(self, followed_username, follower_username, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, follower_username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = follower_username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "follow_user",
                response_status = "response"
            )
            
            response = self._follow_user_controller.handle(
                followed_username,
                follower_username
            )
            return response
        else:
            return False

    def list_user_followers(self, followed_username, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, followed_username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = followed_username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "list_user_followers",
                response_status = "response"
            )
            
            response = self._list_followers_controller.handle(
                followed_username
            )
            return response
        else:
            return False 
    
    def list_user_followeds(self, follower_username, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(
            token,
            follower_username
        )

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = follower_username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "list_user_followeds",
                response_status = "response"
            )
            
            response = self._list_followeds_controller.handle(
                follower_username
            )
            return response
        else:
            return False

    def remove_user_follower(self, followed_username, follower_username, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, follower_username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = follower_username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "remove_user_follower",
                response_status = "response"
            )
            
            response = self._remove_follower_controller.handle(
                followed_username,
                follower_username
            )
            return response
        else:
            return False
    
    def remove_user_followed(self, followed_username, follower_username, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, follower_username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = follower_username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "remove_user_followed",
                response_status = "response"
            )
            
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
        self._coment_post_controller   = ComentPostController()
        self._like_post_controller     = LikePostController()
        self._unlike_post_controller   = UnlikePostController()

        self._ensure_authenticated     = EnsureAuthenticated()
        self._logger                   = Logger()
        
        self._object_name = "User Remote Object"

    def create_post(self, username, description, image, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            if (authed):
                self._logger.new_rmi_log(
                    user_ip_address = "ip default de testes",
                    username        = username,
                    bytes_sent      = 0,
                    bytes_received  = 0,
                    time_spent      = time.time() - begin,
                    nameserver      = "nameserver",
                    object_name     = self._object_name,
                    object_method   = "create_post",
                    response_status = "response"
                )
                
            response = self._create_post_controller.handle(
                username,
                description,
                image
            )
            return response
        else:
            return False

    def list_posts(self, username, target_username, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "list_posts",
                response_status = "response"
            )
            
            response = self._list_posts_controller.handle(
                username,
                target_username
            )
            return response
        else:
            return False
    
    def retrieve_feed(self, username, post_limit, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "retrieve_feed",
                response_status = "response"
            )
            
            response = self._retrieve_feed_controller.handle(
                username,
                post_limit
            )
            return response
        else:
            return False
    
    def coment_post(self, username, post_id, comentary, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "coment_post",
                response_status = "response"
            )
            
            response = self._coment_post_controller.handle(
                username,
                post_id,
                comentary
            )
            
            return response
        else:
            return False
    
    def like_post(self, username, post_id, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "like_post",
                response_status = "response"
            )
            
            response = self._like_post_controller.handle(
                username, 
                post_id
            )
            
            return response
        else:
            return False
    
    def unlike_post(self, username, post_id, token):
        begin = time.time()
        authed = self._ensure_authenticated.handle(token, username)

        if (authed):
            self._logger.new_rmi_log(
                user_ip_address = "ip default de testes",
                username        = username,
                bytes_sent      = 0,
                bytes_received  = 0,
                time_spent      = time.time() - begin,
                nameserver      = "nameserver",
                object_name     = self._object_name,
                object_method   = "unlike_post",
                response_status = "response"
            )
            
            response = self._unlike_post_controller.handle(
                username, 
                post_id
            )
            
            return response
        else:
            return False
    

if (__name__ == "__main__"):

    thread_pool = ThreadPool()
    settings    = Configs().config
    
    remote_object_nameserver = NameServer()
    
    remote_object_nameserver.start(port=settings["server"]["rmi_port"])
    
    remote_object_nameserver.add_remote_object(
        remote_object=UserRemoteObject(),
        name="user_remote_object"
    )
    
    remote_object_nameserver.add_remote_object(
        remote_object=PostRemoteObject(),
        name="post_remote_object"
    )
    
    remote_object_nameserver.loop() 