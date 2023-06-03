import sys
sys.dont_write_bytecode = True





# TODO: NAO PERMITIR MAIS DE UM RELACIONAMENTO ENTRE OS MESMOS USUÁRIOS: SEGUIR DUAS VEZES PELO MESMO USUÁRIO






def get_bytearray_from_file(path):
	with open(path, "rb") as im:
		byte_file = im.read()
		file_ba = bytearray(byte_file)
	return file_ba

def get_file_from_bytearray(ba):
	with open("newImage.png", "wb") as im:
		im.write(ba)


imagem = get_bytearray_from_file("example_img.jpg")


from core.controller import CreateUserController
from core.controller import CreatePostController
from core.controller import FollowUserController
from core.controller import RetrieveFeedController
from core.controller import RemoveFollowerController
from core.controller import RemoveFollowedController

create_user_controller 	   = CreateUserController()
create_post_controller     = CreatePostController()
follow_user_controller     = FollowUserController()
retrieve_feed_controller   = RetrieveFeedController()
remove_follower_controller = RemoveFollowerController()
remove_followed_controller = RemoveFollowedController()

# criando usuário 

# create_user_controller.handle("icaro", "icaro")
# create_user_controller.handle("tome", "tome")

# create_post_controller.handle("icaro", "imagem_aleatoria", imagem)
# create_post_controller.handle("tome", "imagem_aleatoria2", imagem)

follow_user_controller.handle("icaro", "tome")

# retrieve_feed_controller.handle("icaro")

# remove_follower_controller.handle("icaro", "tome")
# remove_followed_controller.handle("tome", "icaro")