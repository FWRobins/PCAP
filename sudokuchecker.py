text = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""
list1 = text.split()
# print(list1)
# string = list(list1[0])
# print(string)

# create lists for lines and columns
lines = ["" for i in range(9)]
columns = [[] for i in range(9)]
for i in range(9):
    lines[i] = list(list1[i])
    for x in range(9):
        columns[x].append(list1[i][x])

#create list of blocks
blocks = ['' for i in range(9)]

for i in range(0,9,3):
    blocks[i] = list(list1[i][:3]+list1[i+1][:3]+list1[i+2][:3])
    blocks[i+1] = list(list1[i][3:6]+list1[i+1][3:6]+list1[i+2][3:6])
    blocks[i+2] = list(list1[i][6:9]+list1[i+1][6:9]+list1[i+2][6:9])

def checklines(x):
    # print(lines[x])
    for i in range(1, 10):
        if str(i) not in lines[x]:
            return False

def checkcolumns(x):
    # print(columns[x])
    for i in range(1, 10):
        if str(i) not in columns[x]:
            return False

def checkblocks(x):
    # print(blocks[x])
    for i in range(1, 10):
        if str(i) not in blocks[x]:
            return False

completed = True
for x in range(9):
    if (checklines(x) or checkcolumns(x) or checkblocks(x)) == False:
        completed = False
        break

print(completed)
