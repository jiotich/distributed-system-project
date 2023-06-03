import socket
import packet_ops as pops
import json
import base64

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
	def wait_requests(self):
		data = None
		while True:
			conn, addr, = self.socket.accept()
			with conn:
				print(f'Conectado por {addr}')

				if addr[0] not in self.current_connections.keys():
					print(f"> Realizando a primera conexao para {addr[0]}")
					self.current_connections[addr[0]] = None

				data = conn.recv(1024)
				operation = json.loads(data.decode())
				if operation["operation_request"] in ["send_image","load_profile"] and not self.verify_auth(addr[0]):
					conn.sendall(b'{"code":"DENIED",\n "response":-1}')
					continue
				else:
					self.current_connections[addr[0]] = operation
					conn.sendall(b'{"code":"OK",\n "response":1234}')
				

				# addr[0] tem o valor do ip, addr[1] o numero da conexao
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
					self.register_user()
					self.operation_finish(addr[0])

				elif not self.verify_auth(addr[0]):
					pass

				data = conn.recv(1024)
				if data == b"CONN_END":
					conn.sendall(bytes("> Transaction ended",encoding='utf-8'))
					break
				

				#packets.append(data)
				#conn.sendall(bytes("> Got Packet",encoding='utf-8'))

		#resp = pops.join_sliced_bytearrays(packets).decode()
		#print(json.loads(resp))

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
					conn.sendall(bytes("> Transaction ended",encoding='utf-8'))
					break
				packets.append(data)
				conn.sendall(bytes("> Got Packet",encoding='utf-8'))
		
		# get_file_from_bytearray() salva o arquivo no diretorio
		# no futuro, os bytes provavelmente serão armazenados no db
		loaded_json = pops.bytearray_to_json(pops.join_sliced_bytearrays(packets))
		pops.get_file_from_bytearray(base64.b64decode(loaded_json["image_bytes"]))
	
	def register_user(self):
		conn, addr, = self.socket.accept()
		data = b""
		with conn:
			print(f'> Registrando usuario para {addr}')
			data = conn.recv(1024)

		loaded_json = pops.bytearray_to_json(data)
		
		# Arquivo de texto usado para propositos de teste
		# TODO: utilizar o db SQL de fato
		# TODO: armazenar hashes das senhas ao inves das senhas em si
		all_users = {}
		with open("users.json", "r") as db:
			all_users = json.loads(db.read())
		
		if loaded_json["username"] not in all_users:
			all_users[loaded_json["username"]] = loaded_json["password"]
		
		with open("users.json", "w") as file:
			json.dump(all_users,file)

	def auth_user(self):
		# TODO: Verificacao de credenciais no banco de dados

		conn, addr, = self.socket.accept()
		data = b""
		with conn:
			print(f'> Validando credenciais para {addr}')
			data = conn.recv(1024)

		loaded_json = pops.bytearray_to_json(data)
		self.authed_users[addr[0]] = loaded_json["username"]

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