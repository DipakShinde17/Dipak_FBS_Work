'''5. Accept a number from user and check if this element is present in the list or
not. Also tell how many times it is present in the list.'''

li = [10,20,30,40,50,40]
searchEle=int(input("Enter number:"))
count=0
for i in range(len(li)):
        if(li[i]==searchEle):
            print(f"{searchEle} is present in this list at {i} index.")
            count+=1

if(count==0):

        print(f"{searchEle} is not present in this list.")
    