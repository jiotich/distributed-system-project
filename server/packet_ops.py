import json
import base64

def get_bytearray_from_file(path, encode=False, no_path=False):
	if no_path:
		return bytearray(json.dumps(path),encoding='utf-8')
	with open(path, "rb") as im:
		byte_file = im.read()
		file_ba = bytearray(byte_file)
	if encode:
		return base64.b64encode(file_ba)
	return file_ba

def slice_bytearray(ba, max_size=1024):
    packets = []
    length = len(ba)
    for i in range(0, length, max_size):
        packets.append(ba[i:i+max_size])
    return packets

def join_sliced_bytearrays(sba):
	joined = bytearray()
	for packet in sba:
		joined += packet
	return joined

def bytearray_to_json(ba):
	res = json.loads(ba)
	return res

def get_file_from_bytearray(ba):
	with open("newImage.png", "wb") as im:
		im.write(ba)

if __name__ == "__main__":
	step1 = get_bytearray_from_file("image.png")
	step2 = slice_bytearray(step1)
	step3 = join_sliced_bytearrays(step2)
	step4 = get_file_from_bytearray(step3)
