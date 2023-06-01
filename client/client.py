import socket
import packet_ops as pops
import json

class Client:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42060
		self.socket = None

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.HOST,self.PORT))

	def send_to_server(self,message):
		self.connect()
		# lembrar que sendall() precisa do parametro encoding="utf-8"
		# caso se esteja trabalhando com texto ao inves de bytes 
		self.socket.sendall(message)
		data = self.socket.recv(1024)

		return data
	
	def send_image(self, image_path):
		response_bytes = self.send_to_server(b'{"operation_request":"send_image"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		if response["response"] == -1:
			print("> Server refused to recieve image.")
			return
		print(1)
		message = {
			"operation": response["response"],
			"image_bytes": pops.get_bytearray_from_file(image_path)
		}
		
		message = bytearray(f"{message}",encoding='utf-8')
		print(2)
		self.send_to_server(b"%s" % message)
		print(2)
		self.send_to_server(b"CONN_END")

if __name__ == "__main__":
	try:
		x = Client()
		x.send_image("image.png")
		#x.send_to_server(b"CONN_END")
	except KeyboardInterrupt:
		x.socket.close()

'''
to_send = get_image_packets(PATH)
for i in to_send:
	send_to_server(i)

send_to_server(b"CONN_END")


while True:
	send_to_server(input("Manda: "))
'''