#Write a Program to input two angles from user and find third angle of the triangle.

A = int(input("Enter 1st angle :"))
B = int(input("Enter 2nd angle :"))

third_angle= 180-(A+B)

print(f"Third angle is {third_angle}")