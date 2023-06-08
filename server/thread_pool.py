from threading       import Thread

class NewThread(Thread):
    def __init__(self, procedure, callback, *args, **kwargs):
        super().__init__()
        self.procedure = procedure
        self.callback  = callback
        self.args      = args
        self.kwargs    = kwargs
        self.result    = None

    def run(self):
        self.result = self.procedure(*self.args, **self.kwargs)
        print(self.result)
        # self.callback(self.result)
        self.callback()

class ThreadPool():
    def __init__(self):
        pass
    # def response_worker_thread(self, value):
        # print(f"work_done, value: {value}")
    def response_worker_thread(selfe):
        print(f"work_done")

    def create_worker_thread(self, procedure, data):
        thread = NewThread(procedure, self.response_worker_thread, data)
        thread.start()
