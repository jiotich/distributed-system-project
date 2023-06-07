import sys
sys.dont_write_bytecode = True

import socket
import packet_ops as pops
import json
import base64
from os import path



from request_handler import RequestHandler
from thread_pool 	 import ThreadPool

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
		self.thread_pool	 = ThreadPool()

	def wait_requests(self):
		data = None
		while True:
			connection, address, = self.socket.accept()
			with connection:
				print(f'Conectado por {address}')
				# address[0] é o ip conectado
				if address[0] not in self.current_connections.keys():
					print(f"> Realizando a primera conexao para {address[0]}")
					self.current_connections[address[0]] = None

				data = connection.recv(1024)
				operation = json.loads(data.decode())
				self.current_connections[address[0]] = operation
				connection.sendall(b'{"code":"OK",\n "response":1234}')

				# dicionario dentro de dicionario
				if self.current_connections[address[0]]["operation_request"] == "send_image":
					print(f"> Realizando operacao de recepcao de imagem para {address[0]}")
					self.request_handler.create_post(self.socket)
					self.operation_finish(address[0])
    
				elif self.current_connections[address[0]]["operation_request"] == "login":
					print(f"Logando usuario: {address[0]}")
					self.request_handler.auth_user(self.socket)
					self.operation_finish(address[0])
				
				elif self.current_connections[address[0]]["operation_request"] == "register_user":
					print(f"Registrando novo usuario: {address[0]}")
					self.request_handler.create_user(self.socket)
					self.operation_finish(address[0])

				elif self.current_connections[address[0]]["operation_request"] == "follow_user":
					print("> Recebida operacao de follow")
					self.request_handler.follow_user(self.socket)
					self.operation_finish(address[0])

				elif self.current_connections[address[0]]["operation_request"] == "retrieve_feed":
					print("> Recebida requisicao por captura do feed")
					self.request_handler.retrieve_feed(self.socket)
					self.operation_finish(address[0])



				data = connection.recv(1024)
				if data == b"CONN_END":
					connection.sendall(bytes("> Transaction ended",encoding='utf-8'))
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