import threading
import time
from tofoli_thread import tofoli_thread

class tofoli_control_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__threads = []
        self.start()


    def run(self):
        while True:
            for t in self.__threads:
                if not t.is_alive():
                    print("Finish thread", t)
                    self.__threads.remove(t)
            time.sleep(0.5)


    def add(self, cmd):
        self.__threads.append(tofoli_thread(cmd))
        self.__threads[self.__threads.__len__()-1].start()
