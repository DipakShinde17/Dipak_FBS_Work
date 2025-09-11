
d = [2000,500,200,100,50,20,10,5]
amount = int(input("Enter number: "))

for note in d:
    if amount >= note: #470 >= 200
        count = amount // note #2
        amount = amount % note #35
        print(f'{note} * {count} ')