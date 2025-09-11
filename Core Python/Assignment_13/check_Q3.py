#3. Python Program to Check if a Given Key Exists in a Dictionary or Not

dict = {"id":"101","name":"dipak","course":"python"}

check = input("Enter key exists or not in dict: ")

if check in dict:
    print("this key is present in this dictionary")
else:
    print("this key is not present in this dictionary")
