#1. Convert the time entered in hh,min and sec into seconds.

seconds=int(input("Enter seconds :"))
temp=seconds

hours= temp // 3600
temp= temp % 3600

minut= temp // 60
temp = temp % 60

second= temp // 60
temp = temp % 60

print(f"hours:- {hours} minut:- {minut} second :-{second}")