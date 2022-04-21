import subprocess
import threading

class tofoli_thread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.__cmd = cmd.split()
        self.__result = ''


    def run(self):
        try:
            self.__result = subprocess \
                .run(self.__cmd, stdout=subprocess.PIPE) \
                .stdout.decode('UTF-8') \
                .__str__() \
                .split('\n')
        except Exception as e:
            self.__result = e.__str__()


    @property
    def result(self): return self.__result
