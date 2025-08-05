#Write a program to check if given 3 digit number is a palindrome or not.

digit=int(input("Enter digit : "))
temp=digit

d1=temp // 100
temp= temp % 100

d2= temp // 10
temp= temp % 10

d3= temp // 1

revers= (d3*100)+(d2*10)+d1
print(f"revers digit : {revers}")

if(revers==digit):
    print("pailindrome number")

else:
    print("not  pailindrome")