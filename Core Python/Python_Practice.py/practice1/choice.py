choice=int(input("Enter choice code (1/2):-"))

if(choice==1):
    print("number is even")
elif(choice==2):
    basic=50
    da=(basic*10)/100
    ta=(basic*20)/100
    hra=(basic*25)/100
    print(f"DA={da} TA={ta} HRA={hra}")
else:
    print("Enter correct choice")