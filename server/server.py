import socket
import packet_ops as pops
import json
import base64

class Server:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42060
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((self.HOST, self.PORT))
		self.socket.listen()

	def wait_requests(self):
		current_connections = {}
		packets = []
		data = None

		while True:
			conn, addr, = self.socket.accept()
			with conn:
				print(f'Conectado por {addr}')

				# o if abaixo representa o inicio de uma operacao requisitada por um cliente
				# a operacao que sera feita e guardada no dicionario current_connections
				# para que essa possa em seguida ser feita
				# ao terminar a operacao, considera-se que o cliente encerrou essa conexao
				if addr[0] not in current_connections.keys():
					print(f"> Realizando a primera conexao {addr[0]}")
					current_connections[addr[0]] = None
					data = conn.recv(1024)
					current_connections[addr[0]] = json.loads(data.decode())
					conn.sendall(b'{"code":"OK",\n "response":1234}')
					#continue
				if current_connections[addr[0]]["operation_request"] == "send_image":
					print(f"> Realizando operacao de envio de imagem para {addr[0]}")
					self.recieve_image()

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
		
		x = pops.join_sliced_bytearrays(packets)
		y = pops.bytearray_to_json(x)
		print(y["image_bytes"])
		pops.get_file_from_bytearray(base64.b64decode(y["image_bytes"]))

if __name__ == "__main__":
	x = Server()
	try:
		while True:	
			x.wait_requests()
	except KeyboardInterrupt:
		print("> Closing server")
		x.socket.close()