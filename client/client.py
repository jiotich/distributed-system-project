import socket
import adrs
import image_ops as imo

HOST = adrs.HOST
PORT = adrs.PORT

PATH = "image.png"

def get_image_packets(path):
	img_ba = imo.get_bytearray_from_file(path)
	packets = imo.slice_bytearray(img_ba)
	return packets

def send_to_server(message):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		# lembrar que sendall() precisa do parametro encoding="utf-8"
		# caso se esteja trabalhando com texto ao inves de bytes 
		s.connect((HOST,PORT))
		s.sendall(bytes(message))

		data = s.recv(1024)
		print(f"Recieved {data}")
		s.close()

to_send = get_image_packets(PATH)
for i in to_send:
	send_to_server(i)

send_to_server(b"CONN_END")

"""
while True:
	send_to_server(input("Manda: "))
"""