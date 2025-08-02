#1. Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:

lenght=int(input("Enter lenght:"))
breadth=int(input("enter breadth:"))
radius=int(input("Enter radius:"))

Area_C= (1/2)*3.14*radius*radius
Reactangle = lenght*breadth

perimeter= (2*lenght) + (3.14*radius)

Area_of_this_figure=Area_C+Reactangle


print(f"Area of this figure : {Area_of_this_figure} perimeter: {perimeter}")