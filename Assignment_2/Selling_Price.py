#WAP to calculate selling price of book based on cost price and discount.
cost_price= int(input("Enter cost price:"))
discount= int(input("Enter discount:"))

dis_amt= cost_price*(10/100)

selling_price=cost_price+dis_amt

print(f"discount_amount={dis_amt} selling_price = {selling_price}")