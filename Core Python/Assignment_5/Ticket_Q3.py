passengers=int(input("Enter passenger: "))
ticket_cost=int(input("Enter ticket amount: "))

total_amount = 0

# Loop to take age of each passenger and calculate fare
for i in range(passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))
    
    if age < 12:
        fare = ticket_cost * 0.70  # 30% discount
    elif age > 59:
        fare = ticket_cost * 0.50  # 50% discount
    else:
        fare = ticket_cost  # full price

    total_amount += fare

print(f"Total ticket amount for all passengers: ₹{total_amount}")