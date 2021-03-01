digitoflife = input("date of birth: (YYYMMDD): ")
digitoflife = list(digitoflife)
numberoflife = 0

while len(digitoflife) > 1:
    for item in digitoflife:
        numberoflife += int(item)
    digitoflife = list(str(numberoflife))
    numberoflife = 0
print(digitoflife[0])
