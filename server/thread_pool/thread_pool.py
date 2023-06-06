from threading import Thread

from core.controller import AuthUserController
from core.controller import CreatePostController
from core.controller import CreateUserController
from core.controller import FollowUserController
from core.controller import RemoveFollowedController
from core.controller import RemoveFollowerController
from core.controller import RetrieveFeedController

class NewThread(Thread):
    def __init__(self, procedure, *args, **kwargs):
        super().__init__()
        self.procedure = procedure
        self.args      = args
        self.kwargs    = kwargs
        self.result    = None

    def run(self):
        self.result = self.procedure(*self.args, **self.kwargs)

class ThreadPool():
    def create_requisiton_handler_thread(controller, data):
        pass