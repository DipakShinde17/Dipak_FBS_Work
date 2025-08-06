import random

userid=input("Enter userid : ")
password=int(input("Enter password : "))
g_captcha=random.randint(1111, 9999)

print(f"enter vaied captcha: {g_captcha}")
captcha=int(input("Enter captcha : "))

if(userid=="admin" and password==12345 and g_captcha==captcha):
    print("successfull")
else:
    print("unsuccessfull")