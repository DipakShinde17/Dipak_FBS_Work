days=int(input("Enter Days :"))
year= days // 365
days= days % 365

week= days // 7
days = days % 7

print(f'Days Calculation : {year} year {week} week {days} days')