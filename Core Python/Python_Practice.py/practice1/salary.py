
basic=int(input("Enter basic:"))

if(basic<=5000):
    da=(basic*10)/100
    ta=(basic*20)/100
    hra=(basic*25)/100
    print(f"DA={da} TA={ta} HRA={hra}")

else:
    da=(basic*15)/100
    ta=(basic*25)/100
    hra=(basic*30)/100
    print(f"da: {da} ta: {ta} hra: {hra}" )


