import socket
import packet_ops as pops
import json
import base64

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
		print("> Sending: ", message[0:100])
		self.socket.sendall(message)
		print("> Sent")
		data = self.socket.recv(1024)
		print(11,data)
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
		print(message["image_bytes"])
		message = bytearray(f"{message}",encoding='utf-8')
		packets = pops.slice_bytearray(message)
		print("> Enviando bytearray")
		for packet in packets:
			packet = packet.decode('utf-8').replace("\'","\"").encode("utf-8")
			self.send_to_server(b"%s" % packet)
		print("> Bytearray enviado")
		self.send_to_server(b"CONN_END")

if __name__ == "__main__":
	try:
		x = Client()
		x.send_image("image.png")
		x.send_to_server(b"CONN_END")
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