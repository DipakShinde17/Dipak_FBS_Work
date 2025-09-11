#5. Python Program to Count the Number of Vowels in a String

str = "dipakshinde"
vowel = 'ieouaIEOUA'
count = 0
for i in str:
    if i in vowel:
        count+=1

print(count)