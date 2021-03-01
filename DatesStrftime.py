import datetime

def myDate(dategiven):
    mydate = datetime.datetime.strptime(dategiven, "%Y/%m/%d %H:%M:%S")
    print(mydate.strftime("%Y/%m/%d %H:%M:%S"))
    print(mydate.strftime("%y/%B/%d %H:%M:%S %p"))
    print(mydate.strftime("%a, %Y %b %d"))
    print(mydate.strftime("%A, %Y %B %d"))
    print("Weekday: ", mydate.strftime("%w"))
    print("Day of the year: ", mydate.strftime("%j"))
    print("Week of the year: ", mydate.strftime("%W"))

myDate("2020/11/04 14:53:00")
