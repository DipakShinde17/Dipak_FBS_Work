age1=int(input("Enter age of 1st person:"))
#age2=int(input("Enter age of 2nd person:"))
#age3=int(input("Enter age of 3rd person:"))
#age4=int(input("Enter age of 4th person:"))
#age5=int(input("Enter age of 5th person:"))
ticket_amt=int(input("Enter ticket amount: "))

if(age1<12):
    dis_amt=ticket_amt*0.3
    amt1=ticket_amt-dis_amt
    print(amt1)
elif(age1>59):
    dis_amt=ticket_amt*0.5
    amt1=ticket_amt-dis_amt
else:
    amt1=ticket_amt