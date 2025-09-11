#11. Python Program to replace every blank space with hyphen in a string.

str = 'shinde dipak is a student of firstbit solution'
str1 = ""

for char in str:
    if(char == " "):
        str1 += "_"
    else:
        str1 += char

print(str1)