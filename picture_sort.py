import os
x = input("Wählen Sie eine Bezeichnung: ")
ordner = os.listdir(os.getcwd())
c=1
for i in ordner:
    if i.endswith(".png"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1
    if i.endswith(".jpg"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1
    if i.endswith(".jpeg"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1
    if i.endswith(".webp"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1
    if i.endswith(".JPG"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1
    if i.endswith(".PNG"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1
    if i.endswith(".JPEG"):
        os.replace(i, str(x)+str(c)+".png")
        c += 1




