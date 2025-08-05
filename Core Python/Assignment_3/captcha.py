import random

user=input("Enter user id:")
password=int(input("Enter password"))
g_captcha=random.randint(1111,9999)

print(f"genarate captcha: {g_captcha}")
captcha=int(input("Enter capcha"))

if(user=="Dipak" and password==1234 and g_captcha==captcha):
    print("login successfull")

else:
    print("login unsuccessfull")
