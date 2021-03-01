text1 = input("enter text1: ")
text2 = input("enter text2: ")

text1 = text1.lower()
text1 = text1.replace(" ", "")
text1len = len(text1)
text1 = list(text1)

text2 = text2.lower()
text2 = text2.replace(" ", "")
text2len = len(text2)
text2 = list(text2)

if text1len != text2len:
    pass
else:
    for elem in range(len(text1)):
        try:
            x = text2.index(text1[elem])
            del text2[x]
        except:
            break
if len(text2) >0:
    print("Not anagrams")
else:
    print("Is anagrams")
    
