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


from core.controller import CreateUserController

createUserController = CreateUserController()
createUserController.handle("Joao", "batata")