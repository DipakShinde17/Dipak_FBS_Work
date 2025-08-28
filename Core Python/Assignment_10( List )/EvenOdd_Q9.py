'''9. Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements.'''

li = [1,2,3,4,5,6,7,8,9,10]
even_li = []
odd_li = []

for i in li:
    if(i % 2==0):
        even_li.append(i)
    else:
        odd_li.append(i)
print("this is the evan list :",even_li)
print("this is the odd list :",odd_li)