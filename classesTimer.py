def formattimer(lst):
    lst = lst[:]
    for i in range(len(lst)):
        if len(str(lst[i])) == 1:
            lst[i] = "0"+str(lst[i])
        else:
            lst[i] = str(lst[i])
    return lst[2]+":"+lst[1]+":"+lst[0]


class Timer:
    def __init__(self, hours, minutes, seconds):
        self.__thetime = [seconds, minutes, hours]

    def __str__(self):
        return formattimer(self.__thetime)

    def next_second(self):
        self.__thetime[0] +=1
        if self.__thetime[0] == 60:
            self.__thetime[0] = 0
            self.__thetime[1] +=1
        if self.__thetime[1] == 60:
            self.__thetime[1] = 0
            self.__thetime[2] += 1
        if self.__thetime[2] == 24:
            self.__thetime[2] = 0
        # print("new time: ", self.__thetime)

    def prev_second(self):
        self.__thetime[0] -=1
        if self.__thetime[0] == -1:
            self.__thetime[0] = 59
            self.__thetime[1] -=1
        if self.__thetime[1] == -1:
            self.__thetime[1] = 59
            self.__thetime[2] -= 1
        if self.__thetime[2] == -1:
            self.__thetime[2] = 23
        # print("new time: ", self.__thetime)



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
