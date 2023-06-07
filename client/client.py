import socket
import packet_ops as pops
import json
import base64

class Client:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42069
		self.socket = None
		self.token = None
		self.username = None

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.HOST,self.PORT))

	def send_to_server(self,message):
		self.connect()
		#print(f"> Sending message [{message}] to server")
		self.socket.sendall(message)
		data = self.socket.recv(1024)
		return data
	
	def send_image(self, image_path, description=""):
		response_bytes = self.send_to_server(b'{"operation_request":"send_image"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		if response["response"] == -1:
			print("> Server refused to recieve image.")
			return
		message = {
			"origin": self.username,
			"image_bytes": pops.get_bytearray_from_file(image_path,encode=True).decode(),
			"description": description
		}
		message = bytearray(f"{message}",encoding='utf-8')
		packets = pops.slice_bytearray(message)
		print("> Enviando bytearray")
		for packet in packets:
			packet = self.fix_quotes(packet)
			self.send_to_server(b"%s" % packet)
		print("> Bytearray enviado")
		answer = self.send_to_server(b"CONN_END")
		loaded_json = json.loads(answer)
		if loaded_json["status_code"] == "200":
			print(f"> Sucesso em seguir postar {image_path}")
		else:
			print(f"> Falha em postar {image_path}")

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

		answer = self.send_to_server(message)
		loaded_json = json.loads(answer)
		self.token = loaded_json["token"]
		self.username = username

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

		answer = self.send_to_server(message)
		loaded_json = json.loads(answer)
		if loaded_json["status_code"] == "200":
			print(f"> Sucesso na criacao do usuario {username}")
		else:
			print(f"> Registro do usuario {username} falhou. O nome provavelmente ja foi registrado, ou contem caracteres invalidos")

	def follow_user(self,username):
		response_bytes = self.send_to_server(b'{"operation_request":"follow_user"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		
		if response["response"] == -1:
			print("> Server refused follow.")
			return
		
		message = {
			"origin": self.username,
			"username": username
		}
		message = bytearray(f"{message}",encoding='utf-8')
		message = self.fix_quotes(message)

		answer = self.send_to_server(message)
		loaded_json = json.loads(answer)
		if loaded_json["status_code"] == "200":
			print(f"> Sucesso em seguir {username}")
		else:
			print(f"> Falha em seguir {username}. O usuario provavelmente nao existe.")
	
	def retrieve_feed(self):
		response_bytes = self.send_to_server(b'{"operation_request":"retrieve_feed"}')
		response = json.loads(response_bytes)
		print("Recieved operation token: ", response["response"])
		
		if response["response"] == -1:
			print("> Server refused retrieve feed.")
			return
		
		message = {
			"operation": response["response"],
			"username": self.username
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
		#x.register_user("sapoboi","boisapo")
		x.login("sapoboi","boisapo")
		#print(x.token,x.username)
		x.send_image("image.png")
		#x.register_user("helio_kitty","mistoquente")
		#x.login("helio_kitty","mistoquente")
		#x.send_image("image.png")
		x.follow_user("thaix")
		#x.send_image("image.png")
		#x.login("icaro","icaro")
		#x.register_user("gaaaalego","portugues")
		#x.send_image("image.png","imagem supimpa. daora demais")
		#x.login("thaix","minax")
		#x.follow_user("icaro")
		x.retrieve_feed()
	except KeyboardInterrupt:
		x.socket.close()
