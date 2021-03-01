import calendar

class MyCalendar():
    def __init__(self, data):
        self.c = calendar.Calendar()
        self.year = data[0]
        self.weekd = data[1]

    def count_weekday_in_year(self):
        count = 0
        for month in range(1,13):
            for data in self.c.monthdays2calendar(self.year, month):
                for tpl in data:
                    if tpl[0] != 0 and tpl[1] == self.weekd:
                        count += 1
        print(count)


tpl = (2019, 0)
MyCalendar(tpl).count_weekday_in_year()
