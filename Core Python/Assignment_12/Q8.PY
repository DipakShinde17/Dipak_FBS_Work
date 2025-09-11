#8. Python Program to Remove the Characters of Odd Index Values in a String

str = "firstbitsolution"
res = ""

for i in range(len(str)):
    if(i % 2 == 0):
        res += str[i]
print(res)
