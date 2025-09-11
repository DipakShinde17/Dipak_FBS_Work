#4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

str = "dipakshinde"
# str1 = ""

for i in range(len(str)):
    str[0],str[10] = str[10],str[0]
print(str)