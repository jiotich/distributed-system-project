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


class UserRemoteObjectInterface:
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
    
    def create_user(self, username, passord, description):
        self._create_user_controller.handle(
            username,
            passord,
            description
        )
    def auth_user(self, username, password):
        self._auth_user_controller.handle(
            username,
            password
        )
    
    def find_user(self, username):
        self._find_user_controller.handle(
            username
        )
        
    def update_user_description(self, username, new_description):
        self._update_user_controller.handle(
            username,
            new_description,
            column="description"
        )
    
    def follow_user(self, followed_username, follower_username):
        self._follow_user_controller.handle(
            followed_username,
            follower_username
        )

    def list_user_followers(self, followed_username):
        self._list_followers_controller.handle(
            followed_username
        )
    
    def list_user_followeds(self, follower_controller):
        self._list_followeds_controller.handle(
            follower_controller
        )
    
    def remove_user_follower(self, followed_username, follower_username):
        self._remove_follower_controller.handle(
            followed_username,
            follower_username
        )
    
    def remove_user_followed(self, followed_username, follower_username):
        self._remove_followed_controller.handle(
            follower_username,
            followed_username
        )
        
class PostRemoteObjectInterface:
    def __init__(self):
        pass