from threading import Thread

# from core.controller import AuthUserController
# from core.controller import CreatePostController
# from core.controller import CreateUserController
# from core.controller import FollowUserController
# from core.controller import RemoveFollowedController
# from core.controller import RemoveFollowerController
# from core.controller import RetrieveFeedController

class NewThread(Thread):
    def __init__(self, id, procedure, callback, *args, **kwargs):
        super().__init__()
        self.thread_id = id
        self.procedure = procedure
        self.callback  = callback
        self.args      = args
        self.kwargs    = kwargs
        self.result    = None

    def run(self):
        self.result = self.procedure(*self.args, **self.kwargs)
        self.callback(self.result)

class ThreadPool():
    def __init__(self):
        self.threads = []
        self.threads_results = []

    def response_worker_thread(self, value):
        print(f"work_done, value: {value}")

    def create_worker_thread(self, procedure, data):
        thread = NewThread(1, procedure, self.response_worker_thread, data)
        thread.start()



def soma(a):
    return a[0]+a[1]

threadPool = ThreadPool()
threadPool.create_worker_thread(soma, [1,2])