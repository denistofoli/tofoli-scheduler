import threading
import time

class tofoli_thread(threading.Thread):
    def __init__(self, name="unnamed", times=3, sleep=1):
        threading.Thread.__init__(self)
        self.__name = name
        self.__times = times
        self.__sleep = sleep
    

    def run(self):
        for i in range(self.__times):
            print(f"{self.__name}...")
            time.sleep(self.__sleep)


    @property
    def name(self): return self.__name
