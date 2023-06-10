import sys
sys.dont_write_bytecode = True

from core.controller import RetrieveUserPostsController
from core.controller import CreateUserController
from core.controller import CreatePostController
from core.controller import FollowUserController
from core.controller import RetrieveFeedController
from core.controller import RetrieveUserPostsController
from core.controller import VerifyIfFollowController

d = VerifyIfFollowController()
x = d.handle("joao","xuxa")
print(x)