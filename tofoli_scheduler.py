from datetime import datetime
import sys
import os
import time
import threading
from tofoli_thread import tofoli_thread

# TODO Load Config File
# TODO Task List
# TODO Task List Iterator
# TODO Update Next Time Run

def clear_threads(threads):
    for j in threads:
        if not j.is_alive():
            threads.remove(j)

    return threads


def main():
    jobs = []
    print("Start")

    jobs.append(tofoli_thread("Thread 1"))
    jobs.append(tofoli_thread("Thread 2", 2, 2))

    for j in jobs: j.start()

    while threading.activeCount() > 1:
        if threading.activeCount() < 3:
            jobs.append(tofoli_thread("Thread 3", 3, 2))
            jobs[jobs.__len__()-1].start()

        jobs = clear_threads(jobs)
        time.sleep(0.5)

    # while True:
    #     for j in jobs:
    #         if j.next_run <= datetime.now().replace(second=0, microsecond=0):
    #             j.run()
    #             print(j.next_run)

        # time.sleep(0.5)

    jobs = clear_threads(jobs)
    print(jobs)

    print("End")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)