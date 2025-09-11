#6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

str = "can i have pen"
str2 = ""

for i in str:
    if (i == " "):
        str2 += "_"
    else:
        str2 += i
print(str2)