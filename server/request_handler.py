from core.controller import AuthUserController
from core.controller import CreateUserController
from core.controller import CreatePostController
from core.controller import FollowUserController
from core.controller import RetrieveFeedController
from core.controller import RemoveFollowerController
from core.controller import RemoveFollowedController

from core.middlewares import EnsureAuthenticated

import packet_ops as pops
import json


class RequestHandler():
    def __init__(self):
        self._create_user_controller     = CreateUserController()
        self._auth_user_controller       = AuthUserController()
        self._create_post_controller     = CreatePostController()
        self._follow_user_controller     = FollowUserController()
        self._retrieve_feed_controller   = RetrieveFeedController()
        self._remove_follower_controller = RemoveFollowerController()
        self._remove_followed_controller = RemoveFollowedController()
        
        self._ensure_authenticated       = EnsureAuthenticated()
        
        self.authed_users = {}
    
    def auth_user(self, socket):
        conn, addr, = socket.accept()
        data = b""
        with conn:
            print(f'> Validando credenciais para {addr}')
            data = conn.recv(1024)
            print(data)
            loaded_json = pops.bytearray_to_json(data)
            user_token = json.loads(self._auth_user_controller.handle(loaded_json["username"],loaded_json["password"]))

            # if user_token["token"] != "-1":
            #     self.authed_users[addr[0]] = loaded_json["username"]
            print(user_token)
            user_token = json.dumps(user_token)		
            conn.sendall(b"%s" % user_token.encode())

    def create_user(self, socket):
        conn, addr, = socket.accept()
        
        data = b""

        with conn:
            print(f'> Registrando usuario para {addr}')
            data = conn.recv(1024)

            loaded_json = pops.bytearray_to_json(data)
		
            return_code = self._create_user_controller.handle(loaded_json["username"],loaded_json["password"])
            conn.sendall(b"%s" % return_code.encode())
    
    def follow_user(self, socket):
        conn, addr, = socket.accept()
        data = b""
        with conn:
            data = conn.recv(1024)

            loaded_json = pops.bytearray_to_json(data)
            
            print(f'> {loaded_json["origin"]} requisita seguir {loaded_json["username"]}')
            # TODO: a operacao abaixo deveria retornar um JSON como resposta do banco
            return_code = self._follow_user_controller.handle(loaded_json["origin"],loaded_json["username"])
            conn.sendall(b"%s" % return_code.encode())
            
    def retrieve_feed(self, socket):
        conn, addr, = socket.accept()
        data = b""
        with conn:
            data = conn.recv(1024)
            loaded_json = pops.bytearray_to_json(data)
            self._retrieve_feed_controller.handle(loaded_json["username"])
            
    def create_post(self, socket):
        packets = []
        data = None
        while True:
            print("> Inicio do recepcao da imagem")
            print("> Esperando aceitacao conexao por parte do cliente")
            conn, addr, = socket.accept()
            with conn:
                print("> Conexao estabelecida")
                print(f'Conectado por {addr}')
                data = conn.recv(1024)
                if data == b"CONN_END":
                    loaded_json = pops.bytearray_to_json(pops.join_sliced_bytearrays(packets))
                    print(loaded_json)
                    return_code = self._create_post_controller.handle(loaded_json["origin"], loaded_json["description"], loaded_json["image_bytes"])
                    print(return_code)
                    conn.sendall(b"%s" % return_code.encode())
                    break
                packets.append(data)
                conn.sendall(bytes("> Got Packet",encoding='utf-8'))