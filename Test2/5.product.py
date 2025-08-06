p1=int(input("Enter 1st product "))
p2=int(input("Enter 2nd product"))
p3=int(input("Enter 3rd product"))
p4=int(input("Enter 4th product"))
p5=int(input("Enter 5th product"))

total_bill=p1+p2+p3+p4+p5

gst=(total_bill*18)/100
total_bill_gst=total_bill+gst

print(f"total bill={total_bill} total bill adding 18% gst={total_bill_gst}")

