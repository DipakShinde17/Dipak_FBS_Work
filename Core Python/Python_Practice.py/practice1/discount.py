price=int(input("Enter price: "))

if(price>=2500):
    dis1= (price*5)/100
    final_price= price- dis1
    print(f"discunt is : {dis1} final price: {final_price}")
    if(price>=5000):
        dis2=(price*10)/100
        final_price1=price-dis2
        print(f" discount is : {dis2} final price {final_price1}")
        
        if(price>=1000):
            dis3=(price*15)/100
            final_price2=price-dis3
            print(f" discount is {dis3} final_price :{final_price2}")
        else:
            print("try to above 1000")
    else:
        print("you try to above 5000")
else:
    print("no discount")