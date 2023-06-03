import sys
sys.dont_write_bytecode = True


def get_bytearray_from_file(path):
	with open(path, "rb") as im:
		byte_file = im.read()
		file_ba = bytearray(byte_file)
	return file_ba

def get_file_from_bytearray(ba):
	with open("newImage.png", "wb") as im:
		im.write(ba)


from core.controller import CreateUserController
from core.controller import CreatePostController


createUserController = CreateUserController()

# a = get_bytearray_from_file("example_img.jpg")


# b = CreatePostController()
# b.handle("Joao", "batata", a)


# createUserController = CreateUserController()
createUserController.handle("leao", "batata")