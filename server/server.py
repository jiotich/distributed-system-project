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
				self.current_connections[addr[0]] = operation
				conn.sendall(b'{"code":"OK",\n "response":1234}')

				# dicionario dentro de dicionario
				if self.current_connections[addr[0]]["operation_request"] == "send_image":
					print(f"> Realizando operacao de recepcao de imagem para {addr[0]}")
					self.request_handler.create_post(self.socket)
					self.operation_finish(addr[0])
    
				elif self.current_connections[addr[0]]["operation_request"] == "login":
					print(f"Logando usuario: {addr[0]}")
					self.request_handler.auth_user(self.socket)
					self.operation_finish(addr[0])
				
				elif self.current_connections[addr[0]]["operation_request"] == "register_user":
					print(f"Registrando novo usuario: {addr[0]}")
					self.request_handler.create_user(self.socket)
					self.operation_finish(addr[0])

				elif self.current_connections[addr[0]]["operation_request"] == "follow_user":
					print("> Recebida operacao de follow")
					self.request_handler.follow_user(self.socket)
					self.operation_finish(addr[0])

				elif self.current_connections[addr[0]]["operation_request"] == "retrieve_feed":
					print("> Recebida requisicao por captura do feed")
					self.request_handler.retrieve_feed(self.socket)
					self.operation_finish(addr[0])



				data = conn.recv(1024)
				if data == b"CONN_END":
					conn.sendall(bytes("> Transaction ended",encoding='utf-8'))
					# breakestablish_follow


	def operation_finish(self,ip):
		self.current_connections[ip]["operation_request"] = None

if __name__ == "__main__":
	x = Server()
	try:
		while True:	
			x.wait_requests()
	except KeyboardInterrupt:
		print("> Closing server")
		x.socket.close()