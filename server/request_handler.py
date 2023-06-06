from core.controller import AuthUserController
from core.controller import CreateUserController
from core.controller import CreatePostController
from core.controller import FollowUserController
from core.controller import RetrieveFeedController
from core.controller import RemoveFollowerController
from core.controller import RemoveFollowedController

import packet_ops as pops

class RequestHandler():
    def __init__(self):
        self._create_user_controller     = CreateUserController()
        self._auth_user_controller       = AuthUserController()
        self._create_post_controller     = CreatePostController()
        self._follow_user_controller     = FollowUserController()
        self._retrieve_feed_controller   = RetrieveFeedController()
        self._remove_follower_controller = RemoveFollowerController()
        self._remove_followed_controller = RemoveFollowedController()
    
    def auth_user(self, conn, addr):
        pass
    
    
    def create_user(self, conn, addr):
        data = b""

        with conn:
            print(f'> Registrando usuario para {addr}')
            data = conn.recv(1024)

            loaded_json = pops.bytearray_to_json(data)
		
            return_code = self.create_user_controller.handle(loaded_json["username"],loaded_json["password"])
            conn.sendall(b"%s" % return_code.encode())
  