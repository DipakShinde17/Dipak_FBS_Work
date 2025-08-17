for i in range(1,10):
    for j in range(1,10-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end="   ")
    print()