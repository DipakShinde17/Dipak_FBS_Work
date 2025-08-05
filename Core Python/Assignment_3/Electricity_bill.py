#write a program to input electricity unit charges and  calculate total electricity bill according to the given  condition.
''' for first 50 units Rs 0.50/ unit
    for next 100 units Rs 0.75/ unit
    for next 100 units Rs 1.20/ unit
    for unit above 250 Rs 1.50/ unit
    An additional surcharge of 20% is added to the bill.'''

unit = int (input("Enter the units : "))

total_bill = 0

if(unit>0):
    if(unit>50):
        if(unit>100):
            if(unit>150 and unit<150 ):
                if(unit>250 ):
                    pass
                else:
                    total_bill=50*0.5
                    unit_1= unit-50

                    total_bill_1=100*0.75
                    unit_2= unit_1-100

                    total_bill_2= 150*1.20
                    unit_3= unit_2-150

                    total_bill_3= unit_3*1.50
                    d= total_bill+total_bill_1+total_bill_2+total_bill_3

                    print(f"The value above 250 units : {d}")
            else:
                total_bill= 50*0.5
                unit_1=unit-50

                total_bill_1=100*0.75
                unit_2 = unit_1-100

                total_bill_2 = unit_2*1.20

                c= total_bill+total_bill_1+total_bill_2
                print(f"The next 150 units of bill : {c}")
        else:
            total_bill= 50*0.5
            unit_1= unit-50

            total_bill_1= unit_1*0.75
           

            print(f"The next 100 units of bill : {total_bill_1+total_bill}")
    else:
        total_bill= unit*0.50
        print(f"The first 50 units of bill : {total_bill}")
else:
    print(f"Enter the correct unit .")