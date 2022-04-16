import threading

# TODO System Calls

class tofoli_thread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.__cmd = cmd

    def run(self):
        print("run", self.__cmd)
