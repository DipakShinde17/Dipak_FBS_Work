sec=int(input("Enter sec="))
temp=sec

h=temp // 3600
temp= temp % 3600

m=temp // 60
temp= temp % 60

s=temp 

print(f"hours={h} minit={m} seconds={s}")