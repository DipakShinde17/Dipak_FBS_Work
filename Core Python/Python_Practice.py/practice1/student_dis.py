price=int(input("Enter price: ") )
student=input("Enter student (yes/not):")

if(student=="yes" and price>500):
    dis=(price*20)/100
    dis1=(price*10)/100
    print(f"you are student than your discount is : {dis}")
    print(f"otherwise your discount is : {dis1}")

elif(student=="not" and price>600):
    dis2=(price*15)/100
    print(f"you are not a student but purchased more than 600:{dis2}" )

else:
    print("no discount")