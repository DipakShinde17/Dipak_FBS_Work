amt=int(input("enter amount"))
temp= amt

two_thousand= temp // 2000
temp = temp % 2000

five_hundred = temp // 500
temp = temp % 500

two_hundred = temp // 200
temp = temp % 200

hundred= temp // 100
temp = temp % 100

fifty= temp // 50
temp = temp % 50

twinty= temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

   
tt= two_thousand+five_hundred+two_hundred+hundred+fifty+twinty+ten

print(f"number of notes {tt}")