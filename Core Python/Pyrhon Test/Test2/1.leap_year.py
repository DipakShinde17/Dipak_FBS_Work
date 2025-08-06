'''Write a program to accept 3 digit number. If first digit is double of second digit and half of
third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
Eg : - 428 , 214 etc.'''

year=int(input("Enter year : "))

if(year%4==0):
    if(year%100==0):
        if(year % 400==0):
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")