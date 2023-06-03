import sys
sys.dont_write_bytecode = True
# from core.services import CreateUserService
# from core.services import AuthUserService

# response_code1 = CreateUserService().execute("icaro", "teste")
# response_code2 = AuthUserService().execute("icaro", "teste")
# print(response_code1)
# print(response_code2)

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
a = get_bytearray_from_file("example_img.jpg")


b = CreatePostController()
b.handle("Joao", "batata", a)


# createUserController = CreateUserController()
# createUserController.handle("Joao", "batata")