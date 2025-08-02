#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount.

amt= int(input("Enter amount"))
temp=amt

a=temp // 2000
temp= temp % 2000

b= temp // 500
temp = temp % 500

c= temp // 200
temp = temp % 200

d= temp // 100
temp = temp % 100

print(f"2000_notes:{a} 500_notes : {b} 200_notes : {c} 100_notes :{d}")
