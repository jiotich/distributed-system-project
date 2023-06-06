import threading
import time

print_lock = threading.Lock()  # Prevent threads from printing at same time.


class TestWorker(threading.Thread):
    # def __init__(self, threadID, name, callback=lambda: None):
    def __init__(self, threadID, name, callback=lambda: None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.callback = callback

    def run(self):
        with print_lock:
            print("Starting " + self.name)
        time.sleep(3)
        with print_lock:
            print("Exiting " + self.name)
        self.callback()

class TestMain:
    def __init__(self):
        self.work_done = False

    def do_work(self):
        thread1 = TestWorker(1, "Thread-1", self.on_work_done)
        thread1.start()
        thread2 = TestWorker(2, "Thread-2", self.on_work_done)
        thread2.start()

    def on_work_done(self, response):
        with print_lock:
            print("work done")
        self.work_done = True

main = TestMain()
main.do_work()
