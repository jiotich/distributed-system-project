import sys
sys.dont_write_bytecode = True

import socket
import packet_ops as pops
import json
import base64

class Client:
	def __init__(self):
		self.HOST = '127.0.0.1'
		self.PORT = 42062
		self.socket = None
		self.token = None
		self.username = None

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.HOST,self.PORT))

	def send_to_server(self,message):
		self.connect()
		print(f"> Sending message [{message}] to server")
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
		print(loaded_json)
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

		packets = []
		while True:
			print(1)
			resp = self.send_to_server(message)
			if resp == b"CONN_END":
				break
			packets.append(resp)

		print()
		feed = pops.join_sliced_bytearrays(packets).decode()
		feed = str(feed).replace("\\","")
		#print(x)
		depth = 0
		all_images = []
		image_jsons = []
		current_image_b64 = ""
		for letter in feed:
			if letter == "[":
				depth+=1
			if depth == 2:
				current_image_b64 += letter
			if letter == "]" and depth == 2:
				all_images.append(current_image_b64)
				current_image_b64 = ""
				depth-=1
		print("Heyo: ",all_images[0])
		# token, descricao, likes, data, hora, dados, dono
		for item in all_images:
			image_jsons.append(json.loads("{\"dados\":%s}" % item))
		#print(image_jsons[0]["dados"][6])
		for item in image_jsons:
			imbytes = base64.b64decode(item["dados"][5])
			pops.get_file_from_bytearray(imbytes,random=True,type="png")

	def fix_quotes(self,message):
		# obviamente tem um jeito melhor de fazer isso
		# mas estou sem tempo
		return message.decode('utf-8').replace("\'","\"").encode("utf-8")

if __name__ == "__main__":
	x = Client()
	try:
		print("> Starting client operations")
		#x.register_user("manovrau","qwerty")
		#x.register_user("honey","qwerty")
		#x.register_user("marcelo","qwerty")
		#x.register_user("jones","qwerty")
		x.login("manovrau","qwerty")
		#x.follow_user("manovrau")
		#x.send_image("image.png")
		#x.register_user("teste12","abacate")
		#x.login("thaix","minax")
		#print(x.token,x.username)
		#x.send_image("image.png")
		#x.follow_user("helio_kitty")
		#x.login("helio_kitty","mistoquente")
		#x.send_image("im.png")
		#x.follow_user("icaro")
		#x.send_image("image.png")
		#x.login("icaro","icaro")
		#x.register_user("gaaaalego","portugues")
		#x.send_image("image.png","imagem supimpa. daora demais")
		#x.login("thaix","minax")
		#x.follow_user("icaro")
		x.retrieve_feed()
	
	except KeyboardInterrupt:
		x.socket.close()
