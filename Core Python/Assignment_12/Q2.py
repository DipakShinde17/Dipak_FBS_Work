#2. Python Program to Remove the nth Index Character from a Non-Empty String

str = "dipakshinde"
emt = ""
n = int(input("Enter you want remove the string index : "))
for i in range(len(str)):
    if(i != n):
        emt += str[i]
print("original string : ",str)
print(emt)