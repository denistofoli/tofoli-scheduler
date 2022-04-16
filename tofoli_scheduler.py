import sys
import os
import time
from datetime import datetime
from tofoli_control_thread import tofoli_control_thread
from tofoli_time_helper import tofoli_time_helper


# TODO Task Class
# TODO Load Config File
# TODO Task List
# TODO Task List Iterator


def main():
    thread_control = tofoli_control_thread()
    jobs = []

    print("Start")

    jobs.append(tofoli_time_helper("2022-01-01", "16:20", "18:04", "t", "m", 1, dows=[1,2,3,4,5,6]))

    while True:
        for j in jobs:
            if j.get_next_run <= datetime.now().replace(second=0, microsecond=0):
                j.next_run()
                thread_control.add("")
        time.sleep(30)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("End")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)