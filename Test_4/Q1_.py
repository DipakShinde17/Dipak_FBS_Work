def demo(num):
   print(f"factors of {num} are: ")
   for i in range(1,num+1):
       if(num % i==0):
           print(i,end=" ")
    
num=int(input("Enter number: "))
demo(num)


