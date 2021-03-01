text1 = input("text string: ").lower()
text2 = input("text to find: ").lower()
hidden = True

for ch in text2:
    position = 0
    if text1.find(ch, position) == -1:
        hidden = False
        break
    else:
        position = text1.find(ch, position)

print(hidden)
