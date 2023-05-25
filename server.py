import socket
import adrs
import image_ops as imo

HOST = adrs.HOST
PORT = adrs.PORT

def join_packets_into_image(packets):
	joined = imo.join_sliced_bytearrays(packets)
	imo.get_file_from_bytearray(joined)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	s.bind((HOST,PORT))
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
	
	join_packets_into_image(packets)