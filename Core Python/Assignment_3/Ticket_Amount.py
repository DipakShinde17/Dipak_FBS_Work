#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :

'''Accept age of five people and also per person ticket amount
and then calculate total amount to ticket to travel for all 
of them based on following condition : 
1. Children below 12 = 30% discount.
2. Senior Citizen (above 59 ) = 50% discount.
3. Others need to pay full.'''


person1 = int(input("Enter age of Person 1 :"))
tic_amt1 = int (input("Enter ticket amount :"))

person2 = int(input("Enter age of Person 2 :"))
tic_amt2 = int(input("Enter the ticket amount :"))

person3 = int(input("Enter age of Person 3 :"))
tic_amt3 = int(input("Enter the ticket amount :"))

person4 = int(input("Enter age of Person 4 :"))
tic_amt4 = int(input("Enter the ticket amount :"))

person5 = int(input("Enter age of Person 5 :"))
tic_amt5 = int(input("Enter the ticket amount : "))



tot_amt = 0

if(person1<12):
    dis_amt= tic_amt1*0.3
    tot_amt = tic_amt1-dis_amt
    print(f"Person 1 Ticket amount after travel :{tot_amt} ")
elif (person1>59):
    dis_amt = tic_amt1*0.5
    tot_amt = tic_amt1-dis_amt
    print(f"Person 1 Ticket amount after travel : {tot_amt}")

else :
    tot_amt= tic_amt1
    print(f"Person 1 Ticket Amount after travel : {tot_amt}")


if(person2<12):
    dis_amt= tic_amt2*0.3
    tot_amt= tic_amt2-dis_amt
    print(f"Person 2 Ticket amount after travel is : {tot_amt}")
elif(person2>59):
    dis_amt= tic_amt2*0.5
    tot_amt= tic_amt2-dis_amt
    print(f"Person 2 Ticket amount after travel : {tot_amt}")
else :
    tot_amt= tic_amt2
    print(f"Person 2 Ticket amount after travel :{tot_amt}")


if(person3<12):
    dis_amt= tic_amt3*0.3
    tot_amt= tic_amt3-dis_amt
    print(f"Person 3 Ticket amount after travel : {tot_amt}")

elif(person3>59):
    dis_amt=tic_amt3*0.5
    tot_amt= tic_amt3-dis_amt
    print(f"Person 3 Ticket amount after travel : {tot_amt}")
else :
    tot_amt= tic_amt3
    print(f"Person 3 Ticket amount after travel : {tot_amt}")

if(person4<12):
    dis_amt=tic_amt4*0.3
    tot_amt= tic_amt4-dis_amt
    print(f"Person 4 Ticket amount after travel : {tot_amt}")

elif(person4>59):
    dis_amt= tic_amt4*0.5
    tot_amt= tic_amt4-dis_amt
    print(f"Person 4 Ticket amount after travel : {tot_amt}")

else: 
    tot_amt= tic_amt4
    print(F"Person 4 ticket amount after travel :{tot_amt}")


if(person5<12):
    dis_amt= tic_amt5*0.3
    tot_amt= tic_amt5-dis_amt
    print(f"Person 5 ticket amount after travel :{tot_amt}")
elif(person5>59):
    dis_amt= tic_amt5*0.5
    tot_amt= tic_amt5-dis_amt
    print(f"Person 5 Ticket amount after travel :{tot_amt}")

else :
    tot_amt= tic_amt5
    print(f"Person 5 Ticket amount after travel : {tot_amt}")