#1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = "abcABC"
empt = ""

for char in str:
    if(char == "a"):
        empt = empt + "$"
    else:
        empt += char
print(empt)





