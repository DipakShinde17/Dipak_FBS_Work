salary=int(input("Enter salary"))

ta=(salary*12)/100
da=(salary*15)/100
hra=(salary*10)/100

total_salary= salary+ta+da+hra

print(f"TA {ta} DA {da} HRA {hra}")
print(total_salary)