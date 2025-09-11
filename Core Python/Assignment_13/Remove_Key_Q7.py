#7. Python Program to Remove the Given Key from a Dictionary

dict = {1:"dipak",2:"shinde",3:"python"}
remove = int(input("Enter key then you removed form dict: "))

if remove in dict:
    del dict[remove]
    print(f"removed this key {remove}")
else:
    print(f"{remove} this key is not present in this list")

print(dict)
