def revers_num(num,rev=0):
   if num==0:
      return rev
   else:
      return revers_num(num//10,rev*10+num%10)

def is_paillindrom(num):
   if num == revers_num(num):
      print(f"{num} is pailindrom ")
   else:
      print(f"{num} is not pailindrom")

num=int(input("Enter number :"))
is_paillindrom(num)




















