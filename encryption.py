text = input("enter text: ")
shift = input("Enter shift value between 1 and 25: ")
while shift.isdigit() == False:
    print("value not a number")
    shift = input("Enter shift value between 1 and 25: ")
while not 1 <= int(shift) <= 25:
    print("value not between 1 and 25")
    shift = input("Enter shift value between 1 and 25: ")
shift = int(shift)
newtext = ""
for ch in text:
    if ch.islower():
        newtext += chr(ord(ch)+shift)
    elif ch.isupper()
    else:
        newtext += ch
print(newtext)
