gender = input("Enter gender (F/M):")
age= int(input("Enter age"))

if((gender == "M" and age >= 21) or (gender == "F" and age>=18)):
    print(f"Eligibility for marrige")

else:
    print(f"pehale jindgi gilo")