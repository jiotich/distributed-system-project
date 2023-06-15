import sys
sys.dont_write_bytecode = True

# from core.controller import RetrieveUserPostsController
# from core.controller import CreateUserController
# from core.controller import CreatePostController
# from core.controller import FollowUserController
# from core.controller import RetrieveFeedController
# from core.controller import RetrieveUserPostsController
# from core.controller import VerifyIfFollowController

# # a = CreateUserController()
# # a.handle("icaro", "batata", "descricao")
# # a.handle("joao", "batata", "descricao")
# # a.handle("tome", "batata", "descricao")
# # a.handle("novo","novo", "descricao")

# # b = CreatePostController()
# # b.handle("icaro", "post icaro", "a")
# # b.handle("joao", "post joao", "a")
# # b.handle("tome", "post tome", "a")

# # c = FollowUserController()
# # c.handle("icaro", "joao")
# # c.handle("tome", "joao")

# # d = RetrieveFeedController()
# # d.handle("joao")

# # e = RetrieveUserPostsController()
# # print(d.handle("joao"))


# # i = VerifyIfFollowController()
# # print(i.handle("joao", "novo"))
# # print(i.handle("novo", "tome"))
# # print(i.handle("joao", "joao"))

# Localiza o servidor de nomes

import Pyro5
from Pyro5.api import Proxy

ns = Pyro5.api.locate_ns(host="localhost", port=9090)
uri = ns

with Proxy("PYRONAME:user_remote_object") as proxy:
    print(proxy.create_user("pyro", "pyro", "pyro"))