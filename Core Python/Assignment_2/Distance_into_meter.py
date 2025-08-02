#Convert distant given in feet and inches into meter and centimeter.
feet=int(input("Enter distance in feet:"))
inches=int(input("Enter distance in inches"))

#1feet=0.3048 meter
#1inches=0.254

total=(feet*0.3040)+(inches*0.254)
meter=int(total)

centimeter= (total-meter)*100

print(centimeter and meter)