import sys
import os
import time
from datetime import datetime
from tofoli_control_thread import tofoli_control_thread
from tofoli_task import tofoli_task


def load_config_tasks():
    tasks = []

    # TODO Load Config File
    tasks.append(tofoli_task("Tarefa de testes",
                             "notify-send task",
                             "2022-01-01",
                             "08:00",
                             "18:00",
                             "t",
                             "m",
                             1,
                             [0,1,2,3,4,5,6]))
    return tasks


def main():
    thread_control = tofoli_control_thread()
    tasks = load_config_tasks()

    print("Start")

    while True:
        for t in tasks:
            if t.get_next_run <= datetime.now().replace(second=0, microsecond=0):
                t.next_run()
                thread_control.add(t.cmd)
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