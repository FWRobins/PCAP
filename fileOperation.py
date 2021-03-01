from os import strerror

try:
    # srcFile = open(input("Source file name? "), "r")
    srcFile = open("text.txt", "r")
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
    data = srcFile.read()
except IOError as e:
    print("error reading file: ", e.errno)
    exit(e.errno)

characters = {}

for ch in data:
    ch = ch.lower()
    if ch == "\n":
        continue
    if ch not in characters:
        characters[ch] = 0
    characters[ch] +=1
print(characters)
listsorted = sorted(characters, key=characters.get, reverse=True)
for k in listsorted:
    try:
        destFile.write("\""+str(k)+"\" ->"+str(characters[k])+"\n")
    except IOError as e:
        print("unable to write to file: ", e.errno)
        exit(e.errno)
srcFile.close()
destFile.close()
