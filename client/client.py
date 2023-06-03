import socket
import packet_ops as pops
import json
import base64

class Client:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42069
		self.socket = None

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.HOST,self.PORT))

	def send_to_server(self,message):
		self.connect()
		print("> Sending message to server")
		self.socket.sendall(message)
		print("> Sent")
		data = self.socket.recv(1024)
		return data
	
	def send_image(self, image_path):
		response_bytes = self.send_to_server(b'{"operation_request":"send_image"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		if response["response"] == -1:
			print("> Server refused to recieve image.")
			return
		message = {
			"operation": response["response"],
			"image_bytes": pops.get_bytearray_from_file(image_path,encode=True).decode()
		}
		message = bytearray(f"{message}",encoding='utf-8')
		packets = pops.slice_bytearray(message)
		print("> Enviando bytearray")
		for packet in packets:
			packet = self.fix_quotes(packet)
			self.send_to_server(b"%s" % packet)
		print("> Bytearray enviado")
		self.send_to_server(b"CONN_END")

	def login(self,username,password):
		response_bytes = self.send_to_server(b'{"operation_request":"login"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		
		if response["response"] == -1:
			print("> Server refused login.")
			return
		
		message = {
			"operation": response["response"],
			"username": username,
			"password": password
		}
		message = bytearray(f"{message}",encoding='utf-8')
		message = self.fix_quotes(message)

		self.send_to_server(message)
	
	def register_user(self,username,password):
		response_bytes = self.send_to_server(b'{"operation_request":"register_user"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		
		if response["response"] == -1:
			print("> Server refused registration.")
			return
		
		message = {
			"operation": response["response"],
			"username": username,
			"password": password
		}
		message = bytearray(f"{message}",encoding='utf-8')
		message = self.fix_quotes(message)

		self.send_to_server(message)

	def fix_quotes(self,message):
		# obviamente tem um jeito melhor de fazer isso
		# mas estou sem tempo
		return message.decode('utf-8').replace("\'","\"").encode("utf-8")

if __name__ == "__main__":
	x = Client()
	try:
		print("> Starting client operations")
		#x.send_image("image.png")
		#x.login("marcelinho","mengao123")
		x.register_user("thaix","minax")
		#x.send_image("image.png")
	except KeyboardInterrupt:
		x.socket.close()
