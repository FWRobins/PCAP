from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __str__(self):
        return "Student data incomplete"


class FileEmpty(StudentsDataException):
    def __str__(self):
        return "No student data"

try:
    # srcFile = open(input("Source file name? "), "r")
    srcFile = open("text2.txt", "r")
except IOError as e:
    print("error opening file: ", e.errno)
    exit(e.errno)
try:
    # destFile = open(input("new file name? "), "w")
    destFile = open("test.txt", "w")
except IOError as e:
    print("error creating new file: ", e.errno)
    exit(e.errno)


try:
    data = srcFile.readlines()
    # print(data)
    # print(len(data))
except IOError as e:
    print("error reading file: ", e.errno)
    exit(e.errno)

students = {}

if len(data) == 0:
    raise FileEmpty

for line in range(len(data)):
    text = data[line].replace("\n", "")
    index = data[line].rfind(" ")
    if text[:index] not in students:
        students[text[:index]] = 0
    try:
        students[text[:index]] += float(text[index+1:])
    except ValueError:
        raise BadLine
    # data[line] = list(data[:data[line].rfind(" ")+1], data[data[line].rfind(" ")+1]:])
    # print(data[line])
# print(students)

for student in students:
    destFile.write(str(student)+"->"+str(students[student])+"\n")
    print(student, students[student])

srcFile.close()
destFile.close()
