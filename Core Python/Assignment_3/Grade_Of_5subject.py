#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1=int(input("Enter mark of 1st subject : "))
m2=int(input("Enter mark of 2nd subject : "))
m3=int(input("Enter mark of 3nd subject : "))
m4=int(input("Enter mark of 4th subject : "))
m5=int(input("Enter mark of 5th subject : "))

total_mark=m1+m2+m3+m4+m5
per= total_mark/500*100

print(f"percentage is : {per}")

if(per>=90):
    print("First Class")
elif(per>=75):
    print("2nd class")
elif(per>=65):
    print("3rd class")
elif(per>55):
    print("4th class")
elif(per>=45):
    print("5th class")
elif(per>=35):
    print("pass")
else:
    print("fail")