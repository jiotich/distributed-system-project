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
        connection, address, = socket.accept()
        data = b""
        with connection:
            print(f'> Validando credenciais para {address}')
            data = connection.recv(1024)
            print(data)
            loaded_json = pops.bytearray_to_json(data)
            user_token = json.loads(self._auth_user_controller.handle(loaded_json["username"],loaded_json["password"]))

            print(user_token)
            user_token = json.dumps(user_token)		
            connection.sendall(b"%s" % user_token.encode())

    def create_user(self, socket):
        connection, address, = socket.accept()
        
        data = b""

        with connection:
            print(f'> Registrando usuario para {address}')
            data = connection.recv(1024)

            loaded_json = pops.bytearray_to_json(data)

            #TODO: passar o json com a descrição 

            return_code = self._create_user_controller.handle(
                loaded_json["username"],
                loaded_json["password"],
                "descrição placeholder"
            )
            
            connection.sendall(b"%s" % return_code.encode())
    
    def follow_user(self, socket):
        connection, address, = socket.accept()
        data = b""
        with connection:
            data = connection.recv(1024)

            loaded_json = pops.bytearray_to_json(data)
            
            print(f'> {loaded_json["origin"]} requisita seguir {loaded_json["username"]}')
            # TODO: a operacao abaixo deveria retornar um JSON como resposta do banco
            return_code = self._follow_user_controller.handle(loaded_json["origin"],loaded_json["username"])
            connection.sendall(b"%s" % return_code.encode())
    

    def send_piece(self, piece, socket):
        connection, address, = socket.accept()
        with connection:
            data = connection.recv(1024)
            connection.sendall(piece)

    def retrieve_feed(self, socket):
        connection, address, = socket.accept()
        data = b""
        packets = []
        with connection:
            data = connection.recv(1024)
            loaded_json = pops.bytearray_to_json(data)
            res = self._retrieve_feed_controller.handle(loaded_json["username"])
            packets = pops.slice_bytearray(pops.get_bytearray_from_file(res,no_path=True))
            
        for packet in packets:
            self.send_piece(packet,socket)
        self.send_piece(b"CONN_END",socket)

    def create_post(self, socket):
        packets = []
        data = None
        while True:
            print("> Inicio do recepcao da imagem")
            print("> Esperando aceitacao conexao por parte do cliente")
            connection, address, = socket.accept()
            with connection:
                print("> Conexao estabelecida")
                print(f'Conectado por {address}')
                data = connection.recv(1024)
                if data == b"CONN_END":
                    loaded_json = pops.bytearray_to_json(pops.join_sliced_bytearrays(packets))
                    print(loaded_json)
                    return_code = self._create_post_controller.handle(loaded_json["origin"], loaded_json["description"], loaded_json["image_bytes"])
                    print(return_code)
                    connection.sendall(b"%s" % return_code.encode())
                    break
                packets.append(data)
                connection.sendall(bytes("> Got Packet",encoding='utf-8'))