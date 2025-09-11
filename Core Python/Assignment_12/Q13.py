#13. Python Program to count number of digits and letters in a string.

str = "12gj3jxj3"
d_count = 0
l_count = 0
for i in str:
    if("0" <= i <= "9"):
        d_count += 1
    elif("a"<= i <= "z" or "A" <= i <= "Z"):
        l_count += 1
print("digit count:",d_count)
print("letter count: ",l_count)