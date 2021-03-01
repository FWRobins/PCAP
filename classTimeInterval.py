from datetime import datetime

class time_interval:
    def __init__(self, time):
        self.time = time.split(":")
        for i in self.time:
            if not i.isnumeric():
                raise TypeError
        self.HS = int(self.time[0])*3600
        self.MS =int(self.time[1])*60
        self.SS = int(self.time[2])
        self.time = self.HS + self.MS + self.SS

    def __str__(self):
        return self.to_str(self.time)

    def to_str(self, time):
        H = int(time/3600)
        M = int((time-H*3600)/60)
        S = time-H*3600-M*60
        return f"{str(H).zfill(2)}:{str(M).zfill(2)}:{str(S).zfill(2)}"

    def __add__(self, other):
        if type(other) == int:
            return self.to_str(self.time+other)
        else:
            return self.to_str(self.time+other.time)

    def __sub__(self, other):
        if type(other) == int:
            if self.time > other:
                return self.to_str(self.time-other)
            else:
                return self.to_str(0)
        else:
            if self.time > other.time:
                return self.to_str(self.time-other.time)
            else:
                return self.to_str(other.time-self.time)

    def __mul__(self, other):
        return self.to_str(self.time*2)


mytime = time_interval("15:33:05")
mytime2 = time_interval("10:01:01")
print(mytime)
print(mytime2)
print(mytime+mytime2)
print(mytime2-mytime)
print(mytime*2)
print(mytime+2)
print(mytime-100000)
print(mytime-100)
