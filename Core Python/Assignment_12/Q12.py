#12. Python Program to count number of lowercase characters in a string.

str = " Python Program To counT."
count = 0

for i in str:
    if 'a' <= i <= 'z':
        count +=1

print(count)