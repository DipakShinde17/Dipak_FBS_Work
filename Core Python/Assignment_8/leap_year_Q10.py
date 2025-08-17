#10. Write a program to check if entered year is a leap year or not.

def year():
    year=int(input("enter year "))

    if(year %  400==0 or year % 4==0 and year % 100!=0):
        print("leap year",year)
    else:
        print("not leap year",year)

year()