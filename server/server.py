import socket

class Server:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42068
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.HOST, self.PORT))
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def wait_requests(self):
		with self.socket as s:
			s.listen()
			packets = []
			data = None

			while True:
				conn, addr, = s.accept()
				with conn:
					print(f'Conectado por {addr}')
					data = conn.recv(1024)
					if data == b"CONN_END":
						conn.sendall(bytes("> Transaction ended",encoding='utf-8'))
						break
					packets.append(data)
					conn.sendall(bytes("> Got Packet",encoding='utf-8'))
					#conn.sendall(bytes("sapa bonde: ",encoding='utf-8')+ data)

x = Server()			
x.wait_requests()