import socket

class Client:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42068
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	def send_to_server(self,message):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			# lembrar que sendall() precisa do parametro encoding="utf-8"
			# caso se esteja trabalhando com texto ao inves de bytes 
			s.connect((self.HOST,self.PORT))
			s.sendall(bytes(message))

			data = s.recv(1024)
			print(f"Recieved {data}")
			s.close()

x = Client()
x.send_to_server(b"aaaaa")
'''
to_send = get_image_packets(PATH)
for i in to_send:
	send_to_server(i)

send_to_server(b"CONN_END")


while True:
	send_to_server(input("Manda: "))
'''