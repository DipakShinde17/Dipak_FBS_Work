import random

user_id = (input("Enter the use Id:- "))
password = int(input("Enter the password:-"))
generate_captcha= random.randint(1111,9999)

print(f"captcha: {generate_captcha}")
captcha=int(input("enter capcha"))

if(user_id=="Dipak" and password==1234 and generate_captcha=="captcha"):
    print("logoin sucessfull")

else:
    print("logint unscessfull")

