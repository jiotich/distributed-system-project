import sys
sys.dont_write_bytecode = True

import socket
import packet_ops as pops
import json
import base64
from os import path



from request_handler import RequestHandler

class Server:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42069
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((self.HOST, self.PORT))
		self.socket.listen()
		self.current_connections = {}
		self.authed_users = {}
  
		self.request_handler = RequestHandler()

	def wait_requests(self):
		data = None
		while True:
			conn, addr, = self.socket.accept()
			with conn:
				print(f'Conectado por {addr}')
				# addr[0] é o ip conectado
				if addr[0] not in self.current_connections.keys():
					print(f"> Realizando a primera conexao para {addr[0]}")
					self.current_connections[addr[0]] = None

				data = conn.recv(1024)
				operation = json.loads(data.decode())
				if operation["operation_request"] not in ["register_user","login"] and not self.verify_auth(addr[0]):
					conn.sendall(b'{"code":"DENIED",\n "response":-1}')
					continue
				else:
					self.current_connections[addr[0]] = operation
					conn.sendall(b'{"code":"OK",\n "response":1234}')

				# dicionario dentro de dicionario
				if self.current_connections[addr[0]]["operation_request"] == "send_image":
					print(f"> Realizando operacao de recepcao de imagem para {addr[0]}")
					self.recieve_image()
					self.operation_finish(addr[0])
				
				elif self.current_connections[addr[0]]["operation_request"] == "login":
					print(f"Logando usuario: {addr[0]}")
					self.auth_user()
					self.operation_finish(addr[0])
				
				elif self.current_connections[addr[0]]["operation_request"] == "register_user":
					print(f"Registrando novo usuario: {addr[0]}")
     
					conn, addr, = self.socket.accept()
     
					self.request_handler.create_user(conn, addr)
					self.operation_finish(addr[0])

				elif self.current_connections[addr[0]]["operation_request"] == "follow_user":
					print("> Recebida operacao de follow")
					self.establish_follow()
					self.operation_finish(addr[0])

				elif self.current_connections[addr[0]]["operation_request"] == "retrieve_feed":
					print("> Zumzum")
					self.retrieve_feed()
					self.operation_finish(addr[0])

				data = conn.recv(1024)
				if data == b"CONN_END":
					conn.sendall(bytes("> Transaction ended",encoding='utf-8'))
					# breakestablish_follow

	def recieve_image(self):
		packets = []
		data = None
		while True:
			print("> Inicio do recepcao da imagem")
			print("> Esperando aceitacao conexao por parte do cliente")
			conn, addr, = self.socket.accept()
			with conn:
				print("> Conexao estabelecida")
				print(f'Conectado por {addr}')
				data = conn.recv(1024)
				if data == b"CONN_END":
					loaded_json = pops.bytearray_to_json(pops.join_sliced_bytearrays(packets))
					return_code = self.create_post_controller.handle(self.authed_users[addr[0]], loaded_json["description"], loaded_json["image_bytes"])
					print(return_code)
					conn.sendall(b"%s" % return_code.encode())
					break
				packets.append(data)
				conn.sendall(bytes("> Got Packet",encoding='utf-8'))


	def auth_user(self):
		# TODO: Verificacao de credenciais no banco de dados
		conn, addr, = self.socket.accept()
		data = b""
		with conn:
			print(f'> Validando credenciais para {addr}')
			data = conn.recv(1024)

			loaded_json = pops.bytearray_to_json(data)
			user_token = json.loads(self.auth_user_controller.handle(loaded_json["username"],loaded_json["password"]))
			#print(loaded_json)
			if user_token["token"] != "-1":
				self.authed_users[addr[0]] = loaded_json["username"]

			user_token = json.dumps(user_token)		
			conn.sendall(b"%s" % user_token.encode())
	
	def establish_follow(self):
		conn, addr, = self.socket.accept()
		data = b""
		with conn:
			data = conn.recv(1024)

			loaded_json = pops.bytearray_to_json(data)
			print(f'> {self.authed_users[addr[0]]} requisita seguir {loaded_json["username"]}')
			# TODO: a operacao abaixo deveria retornar um JSON como resposta do banco
			return_code = self.follow_user_controller.handle(self.authed_users[addr[0]],loaded_json["username"])
			conn.sendall(b"%s" % return_code.encode())

	def retrieve_feed(self):
		conn, addr, = self.socket.accept()
		data = b""
		with conn:
			data = conn.recv(1024)
			loaded_json = pops.bytearray_to_json(data)
			self.retrieve_feed_controller.handle(loaded_json["username"])

	def operation_finish(self,ip):
		self.current_connections[ip]["operation_request"] = None
	
	def verify_auth(self,ip):
		return 1 if ip in self.authed_users else 0	

if __name__ == "__main__":
	x = Server()
	try:
		while True:	
			x.wait_requests()
	except KeyboardInterrupt:
		print("> Closing server")
		x.socket.close()