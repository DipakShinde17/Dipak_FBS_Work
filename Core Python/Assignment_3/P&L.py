#Write a program to calculate profit or loss.

cost_price=int(input("Enter cost price: "))
selling_price= int(input("Enter selling price: "))

if(cost_price < selling_price):
    print("profit")

else:
    print("loss")