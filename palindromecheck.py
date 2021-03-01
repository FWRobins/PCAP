text = input("Enter your sentance here(text only): ")
text = text.lower()
text = text.replace(" ", "")
halfcount = len(text)//2
palin = True
for x in range(halfcount+1):
    if text[x] != text[x*-1-1]:
        palin = False
        break
    
print(palin)
