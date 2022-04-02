# t = time interval (Ok)
# group = "t"
    # m = minutites / h = hours / d = Daily
        # interval = 12

    # dow = [2,3]
        # 0 = monday
        # 1 = tuesday
        # 2 = wednesday
        # 3 = thursday
        # 4 = friday
        # 5 = saturday
        # 6 = sunday

# m = monthly
# group = "m"
    # type_interval
        # f = First Day
        # l = Last Day
        # d = Day Fixed
    # day_fixed = 15


from datetime import datetime, timedelta

class tofoli_time_helper():
    def __init__(self, start_date, start_time, end_time, group, type_interval, interval=1, day_fixed=0, dows=[0,1,2,3,4,5,6]):
        self.__start_date = start_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__start_run = self.__valid(self.__start_date + " " + start_time, "%Y-%m-%d %H:%M")
        self.__group = group
        self.__type_interval = type_interval
        self.__interval = interval
        self.__dows = dows
        self.__day_fixed = day_fixed
        self.__next_run = self.__start_run

        self.__set_start_run()
        self.next_run()


    def __valid(self, date_time, valid_format):
        date_obj = None

        try:
            date_obj = datetime.strptime(date_time, valid_format)
        except ValueError:
            print("*** Invalid date-time ***")

        return date_obj


    def __next_dow(self, date):
        while date.weekday() not in self.__dows:
            date += timedelta(days=1)

        return date
    
    def __next_month(self, date):
        old_month = date.__str__()[5:7]

        while date.__str__()[5:7] == old_month:
            date += timedelta(days=15)

        return date


    def __set_start_run(self):
        if self.__group == "m":
            month = self.__next_month(self.__start_run).__str__()[:8]

            if self.__type_interval == "f":
                self.__start_run = self.__valid(month + "01 " + self.__start_time, "%Y-%m-%d %H:%M")
            elif self.__type_interval == "l":
                self.__start_run = self.__valid(month + "01 " + self.__start_time, "%Y-%m-%d %H:%M") - timedelta(days=1)
            else:
                self.__start_run = self.__valid(month + self.__day_fixed.__str__() + " " + self.__start_time, "%Y-%m-%d %H:%M")
        else:
            self.__start_run = self.__next_dow(self.__start_run)

        self.__next_run = self.__start_run


    def next_run(self):
        now = datetime.now().replace(second=0, microsecond=0)

        if self.__next_run <= now and self.__group == "t":
            self.__next_run = self.__valid(now.__str__()[:10] + " " + self.__start_time, "%Y-%m-%d %H:%M")
            self.__next_run = self.__next_dow(self.__next_run)

        while self.__next_run <= now:
            if self.__group == "t":
                if self.__type_interval == "m":
                    delta = timedelta(minutes=self.__interval)
                elif self.__type_interval == "h":
                    delta = timedelta(hours=self.__interval)
                elif self.__type_interval == "d":
                    delta = timedelta(days=self.__interval)
                else:
                    exit
            elif self.__group == "m":
                delta = timedelta(month=1)

            self.__next_run += delta

        return

    @property
    def get_next_run(self): return self.__next_run