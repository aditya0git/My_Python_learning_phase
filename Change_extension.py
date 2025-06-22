# Renames all files in the current directory to a specified extension,
# skipping the script itself and handling name conflicts safely.


import os

x = input("Enter desired extension : ")
FileName = os.path.basename(__file__)

AllFiles = os.listdir()
a = 0
b = 0
c = 0

for i in AllFiles :
    y = (i.split(sep = ".", maxsplit = 1))[0]

    if i == FileName :
        continue

    if i == (y + x) :
        b += 1
        continue

    try :
        os.rename(i, y + x)
    except FileExistsError :
        c += 1
        os.rename(i, y + " (" + str(c) + ")" + x)
    else :
        a += 1
    
print(f"{a} file(s) extension changed")
print(f"{b} file(s) had same extension as desired")
print(f"{c} file(s) had duplicate first name")
