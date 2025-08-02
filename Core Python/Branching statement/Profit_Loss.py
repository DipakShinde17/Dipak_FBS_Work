cost_price=int(input("Enter cost price"))
selling_price=int(input("Enter selling price"))

temp=cost_price + selling_price

if(cost_price <= selling_price):
    profit_amount= selling_price - cost_price
    total_amount= profit_amount + cost_price
    print(f"total amount = {total_amount} and profit amount = {profit_amount}")

else:
    loss= selling_price - cost_price
    print(f"the loss is {loss}")

