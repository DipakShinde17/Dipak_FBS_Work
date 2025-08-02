days=int(input("Enter days: "))
year= days // 365
days= days % 365

week= days // 7
days= week % 7

print(f"year {year} weeks {week} days {days}")