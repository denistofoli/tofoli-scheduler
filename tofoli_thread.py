import subprocess
import threading

class tofoli_thread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.__cmd = cmd.split()
        self.__std_out = ''


    def run(self):
        self.__std_out = subprocess \
                    .run(self.__cmd, stdout=subprocess.PIPE) \
                    .stdout.decode('UTF-8') \
                    .__str__() \
                    .split('\n')


    @property
    def std_out(self): return self.__std_out
