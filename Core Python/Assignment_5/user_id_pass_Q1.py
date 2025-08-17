''' Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.'''

user_id=(input("Enter User_id :"))
password=int(input("Enter password:"))

if(user_id=="dipak" and password==1234):
    print("password and user id correct")
    #for i in range(1,4):
    print("correct ")
else:
    for i in range(1,4):
        print("try")