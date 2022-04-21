from tofoli_time_helper import tofoli_time_helper

class tofoli_task():
    def __init__(self,
                 name,
                 cmd,
                 start_date,
                 start_time,
                 stop_time,
                 group,
                 interval_type,
                 interval,
                 dows):
        self.__name = name
        self.__cmd = cmd
        self.timer = tofoli_time_helper(start_date,
                                        start_time,
                                        stop_time,
                                        group,
                                        interval_type,
                                        interval,
                                        dows)
